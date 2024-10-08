from deephaven import empty_table, time_table, agg
import random
import string
# from deephaven import ema_time
from deephaven.plot.figure import Figure

#letters_upp = string.ascii_uppercase
mock_array = ['A','B','C','D','E']


# Create static tables
static_table = empty_table(26300).update(
    [
        "Price = randomDouble(1, 100)",
        "Timestamp = parseInstant(`2024-01-01T01:00 ET`) + i * HOUR",
        "Ticker = (String)mock_array[(int)(randomInt(0, 5))]",
    ]
)



# mock a streaming data use time_table
ticking_table = time_table("PT1S").update(
    [
        "Price = randomDouble(1, 100)",
        "Ticker = (String)mock_array[(int)(randomInt(0, 5))]",
    ]
)

filtered_ticking_table = ticking_table.where("Price > 50")
rollup_by_ticker = ticking_table.rollup(
    aggs=[agg.avg("Price")],  # Calculate the average Price
    by=["Ticker"]              # Group by Ticker
)

plot_line_1 = Figure().plot_xy(series_name="Price", t=ticking_table, x="Timestamp", y="Price").show()
