import QuantLib as ql


# maturity_date = ql.Date(29, 8, 2023)
# spot_price = 179.88
# strike_price = 180
# dividend_rate = 0.0053

def book_example():
    # AAPL Example using Heston and BSM models

    strike_price = 110.0
    payoff = ql.PlainVanillaPayoff(ql.Option.Call, strike_price)
    # option data
    maturity_date = ql.Date(15, 1, 2016)
    spot_price = 127.62
    strike_price = 130
    volatility = 0.20  # the historical vols for a year
    dividend_rate = 0.0163
    option_type = ql.Option.Call
    risk_free_rate = 0.001
    day_count = ql.Actual365Fixed()
    calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
    calculation_date = ql.Date(8, 5, 2015)
    ql.Settings.instance().evaluationDate = calculation_date
    ql.Settings.instance().evaluationDate = calculation_date
    payoff = ql.PlainVanillaPayoff(option_type, strike_price)
    exercise = ql.EuropeanExercise(maturity_date)
    european_option = ql.VanillaOption(payoff, exercise)
    v0 = volatility * volatility
    kappa = 0.1
    theta = v0
    sigma = 0.1
    rho = -0.75
    spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot_price))
    flat_ts = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, risk_free_rate, day_count))
    dividend_yield = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, dividend_rate, day_count))
    heston_process = ql.HestonProcess(flat_ts, dividend_yield,
                                      spot_handle, v0, kappa,
                                      theta, sigma, rho)
    engine = ql.AnalyticHestonEngine(ql.HestonModel(heston_process), 0.01, 1000)
    european_option.setPricingEngine(engine)
    h_price = european_option.NPV()
    print("The Heston model price is {0}".format(h_price))
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(calculation_date, calendar,
                            volatility, day_count)
    )
    bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_yield, flat_ts, flat_vol_ts)
    european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
    bs_price = european_option.NPV()
    print("The Black-Scholes-Merton model price is {0}".format(bs_price))


book_example()

# The Heston model price is 6.533855481449102
# The Black-Scholes-Merton model price is 6.749271812460607

# The Heston model price is 32.07094065113685
# The Black-Scholes-Merton model price is 36.66913703572554
