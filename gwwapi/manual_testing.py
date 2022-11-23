import client as cli 

a = cli.get_reservoir_ts(84765).json()
print(len(cli.to_timeseries(a)))

m = cli.get_reservoir_ts_fitted(84765).json()
print(len(cli.to_timeseries(m)))
