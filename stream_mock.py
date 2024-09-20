# run deephaven sever in local host: deephaven server --jvm-args "-Xmx4g -Dauthentication.psk=1111"

import random
from deephaven import time_table
from deephaven.column import string_col, double_col, long_col

ticking_table = time_table("PT1s")  # Ticks every 1 second

# Define a function to generate random data and update the table
#def update_table():
    # Generate random data
ticker = random.choice(["A", "B", "C", "D", "E"])
price = round(random.uniform(100.0, 1500.0), 2)  # Random price between 100 and 1500

    # Create a table with the new row of data
updated_table = ticking_table.update_view([
        f"Ticker = '{ticker}'",  # Ensure Ticker is a string literal
        f"Price = {price:.2f}",  # Ensure Price is a double
])

    #return updated_table

# Create the initial table with an empty state
initial_table = time_table("PT1s")

# Combine the initial table with the dynamic updates
streaming_table = updated_table

# Print the table to confirm
print(streaming_table)
