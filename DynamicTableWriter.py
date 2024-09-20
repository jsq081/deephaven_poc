from deephaven import DynamicTableWriter
from deephaven.column import long_col, double_col
import deephaven.dtypes as dht
import time
from deephaven import time_table
col_def = {"Num": dht.long, "Ticker":dht.string}
writer = DynamicTableWriter(col_def)

result = writer.table



writer.write_row(1.6566, "A")
time.sleep(3)
writer.write_row(2.522, "B")
time.sleep(3)
writer.write_row(3.54, "C")
time.sleep(3)
writer.write_row(4.556, "D")
