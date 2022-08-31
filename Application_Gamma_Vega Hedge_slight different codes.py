import sys

sys.path.append('/Users/jktrading/PycharmProjects/Dynamic Hedge_Option')
import Dynamic_Hedge as DH
import numpy as np

size = -1000
nvda_call_545 = DH.EuropeanCall(543, .53, 545, 30 / 365, .015)
# Todo pay attention to why using [[]], since it is for matrix calcualtion in the final step
short_nvda_call_545_greeks = [[nvda_call_545.delta * size], [nvda_call_545.gamma * size], [nvda_call_545.vega * size]]
print('short_nvda_call_545_greeks: \n', short_nvda_call_545_greeks)

nvda_call_550 = DH.EuropeanCall(543, .53, 550, 30 / 365, .015)
short_nvda_call_550_greeks = [nvda_call_550.delta, (nvda_call_550.gamma), (nvda_call_550.vega)]
print('short_nvda_call_550_greeks: \n', short_nvda_call_550_greeks)

nvda_call_555 = DH.EuropeanCall(543, .53, 555, 30 / 365, .015)
short_nvda_call_555_greeks = [nvda_call_555.delta, (nvda_call_555.gamma), (nvda_call_555.vega)]
print('short_nvda_call_555_greeks: \n', short_nvda_call_555_greeks)

greeks_matrix = np.array([[nvda_call_550.gamma, nvda_call_555.gamma], [nvda_call_550.vega, nvda_call_555.vega]])
required_portfolio_greeks = [[nvda_call_545.gamma * size * -1], [nvda_call_545.vega * size * -1]]
print('option gamma and vega matrix: \n', greeks_matrix)
print('portfolio greeks: \n', required_portfolio_greeks)

# Todo [greeks_matrix][weighting]=-[portfolio greeks matrix], negative since it is the required amt to net off it
# Todo therefore [weighting] = [pga]/[g_m]= [pga]*[g_m]^-1
# Todo, ^-1 means invert [g_m], just refer to the graph I drawn to illustrate the concept
inv = np.linalg.inv(np.round(greeks_matrix, 2))
print('inverse matrix of greeks: \n', inv)
w = np.dot(inv, required_portfolio_greeks)
print('desired weighting of options: \n', w)

# Todo W*greeks_matrix should equal to the required greeks to net off the portfolio greeks
# Todo must put the matrix first, otherwise calculation error.
# Todo matrix multiplication rule AB is not equal to BA, row1*col1...
checking = np.round(np.dot(np.round(greeks_matrix, 2), w) - required_portfolio_greeks)
print('checking: \n', checking)

# Todo, the position of Delta, Gamma, Vege must align
greeks_matrix1 = np.array([[nvda_call_550.delta, nvda_call_555.delta], [nvda_call_550.gamma, nvda_call_555.gamma],
                           [nvda_call_550.vega, nvda_call_555.vega]])
portfolio_greeks1 = np.round(np.dot(np.round(greeks_matrix1, 2), w) + short_nvda_call_545_greeks)
print('greeks of options: \n', greeks_matrix1)
print('portfolio greeks: \n', short_nvda_call_545_greeks)
print('final portfolio greeks: \n', portfolio_greeks1)
