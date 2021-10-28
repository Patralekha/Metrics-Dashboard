from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from prometheus_flask_exporter import PrometheusMetrics
import pymongo
import logging, os, random, opentracing
from flask_pymongo import PyMongo
from flask_opentracing import FlaskTracing
from jaeger_client import Config

from opentelemetry import trace

from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
)

trace.set_tracer_provider(TracerProvider(resource=Resource.create({SERVICE_NAME: "backend-service"})))
# Create the exporter for jaeger
jaeger_exporter = JaegerExporter()

# Add the exporter to the spanner
spanner = BatchSpanProcessor(jaeger_exporter)

# Make sure it is added here
trace.get_tracer_provider().add_span_processor(spanner)

# make sure to define the tracer here
tracer = trace.get_tracer(__name__)

# Define the app, the Prometheus Metrics and the instrumentor for Flask, also determine the server used

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app, excluded_urls="metrics")
gunicorn_app = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
if gunicorn_app:
    metrics = GunicornInternalPrometheusMetrics(app)
else:
    metrics = PrometheusMetrics(app)
    
#trace.set_tracer_provider(TracerProvider())
#trace.get_tracer_provider().add_span_processor(
#    SimpleExportSpanProcessor(ConsoleSpanExporter())
#)

#app = Flask(__name__)
#metrics = GunicornInternalPrometheusMetrics(app)

#FlaskInstrumentor().instrument_app(app)
#RequestsInstrumentor().instrument()

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)



def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%pat(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer('backend-service')
tracing = FlaskTracing(tracer,True,app)
flask_head_tracing = tracing.get_span()

@app.route('/')
def homepage():
    with opentracing.tracer.start_span("base-endpoint", child_of=flask_head_tracing) as span:
        return "Hello World"


@app.route('/api')
def my_api():
    with opentracing.tracer.start_span("api-endpoint", child_of=flask_head_tracing) as span:
        answer = "something"
        span.set_tag("answer", answer)
        return jsonify(repsonse=answer)


@app.route('/star', methods=['POST'])
def add_star():
    with opentracing.tracer.start_span("star-endpoint", child_of=flask_head_tracing) as span:
       star = mongo.db.stars
       name = request.json['name']
       distance = request.json['distance']
       star_id = star.insert({'name': name, 'distance': distance})
       new_star = star.find_one({'_id': star_id })
       output = {'name' : new_star['name'], 'distance' : new_star['distance']}
       return jsonify({'result' : output})


@app.route('/errors')
def error_message():
    errors_choice = [400,500]
    return jsonify({"error": "Error endpoint",}), random.choice(errors_choice)


metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)

if __name__ == "__main__":
    app.run()
