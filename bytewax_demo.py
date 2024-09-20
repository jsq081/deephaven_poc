from datetime import timedelta
from bytewax.dataflow import Dataflow
from bytewax.connectors.demo import RandomMetricSource
import bytewax.operators as op
from bytewax.connectors.stdio import StdOutSink
from bytewax.run import run

# Create the RandomMetricSource to generate random metrics
x = RandomMetricSource(metric_name="metric_name", interval=timedelta(seconds=1))

# Define the dataflow
flow = Dataflow("my_first_bytewax_dataflow")
input_stream = op.input("input", flow, x)
op.output("output", input_stream, StdOutSink())

# Execute the dataflow
if __name__ == "__main__":
    print("Starting dataflow execution...")
    run(flow)
