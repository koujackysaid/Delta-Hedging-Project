import sys

sys.path.append('/Users/jktrading/PycharmProjects/Dynamic Hedge_Option')
import Dynamic_Hedge as DH

short_nvda = DH.EuropeanCall(543, .53, 545, 30 / 365, .015)
print('call option price_nvda: \n', short_nvda.price * (1000))

print('call option delta_nvda: \n', short_nvda.delta * (-1000))
print('call option gamma_nvda: \n', short_nvda.gamma * (-1000))
print('call option vega_nvda: \n', short_nvda.vega * (-1000))

call_a = DH.EuropeanCall(543, .53, 550, 30 / 365, .015)
print('call option delta_a: \n', call_a.delta)
print('call option gamma_a: \n', call_a.gamma)
print('call option vega_a: \n', call_a.vega)

call_b = DH.EuropeanCall(543, .53, 555, 30 / 365, .015)
print('call option delta_b: \n', call_b.delta)
print('call option delta_b: \n', call_b.gamma)
print('call option delta_b: \n', call_b.vega)

import numpy as np

greeks = np.array([[call_a.gamma, call_b.gamma], [call_a.vega, call_b.vega]])
portfolio_greeks = [[short_nvda.gamma * 1000], [short_nvda.vega * 1000]]
print('Gamma and Vega of option a and option b: \n', greeks)
print('Gamma and Vega of portfolio greeks: \n', portfolio_greeks)

# We need to round otherwise we can end up with a non-invertible matrix
inv = np.linalg.inv(np.round(greeks, 2))
print('inverse matrix of greeks: \n', inv)

w = np.dot(inv, portfolio_greeks)
print('desired weighting of option a and option b: \n', w)

# Greeks including delta
portfolio_greeks = [[short_nvda.delta * -1000], [short_nvda.gamma * -1000], [short_nvda.vega * -1000]]
greeks = np.array([[call_a.delta, call_b.delta], [call_a.gamma, call_b.gamma], [call_a.vega, call_b.vega]])
print('greeks of options: \n', greeks)
print('portfolio greeks: \n', portfolio_greeks)
print('portfolio greeks after hedging with options: \n', np.round(np.dot(np.round(greeks, 2), w) + portfolio_greeks))
