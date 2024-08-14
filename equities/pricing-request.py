import QuantLib as ql
# import numpy as np
# import math


strike_price = 110.0
payoff = ql.PlainVanillaPayoff(ql.Option.Call, strike_price)
# option data
maturity_date = ql.Date(15, 1, 2016)
spot_price = 127.62
strike_price = 130
volatility = 0.20 # the historical vols for a year
dividend_rate = 0.0163
option_type = ql.Option.Call
risk_free_rate = 0.001
day_count = ql.Actual365Fixed()
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
calculation_date = ql.Date(8, 5, 2015)
ql.Settings.instance().evaluationDate = calculation_date
