import pandas as pd
dates = pd.Series(['2025-01-01', '2025-02-15', '2025-03-20'])
timeseries = pd.to_datetime(dates)
print(timeseries)