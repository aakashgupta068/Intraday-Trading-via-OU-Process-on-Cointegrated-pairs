import numpy as np
import statsmodels.api as sm

def estimate_ou_parameters(spread):
    spread = spread.dropna()
    X = sm.add_constant(spread.shift(1).dropna())
    Y = spread[1:].loc[X.index]
    model = sm.OLS(Y, X).fit()
    a, b = model.params
    resid_std = np.std(model.resid)

    theta = -np.log(b)
    mu = a / (1 - b)
    sigma = resid_std * np.sqrt(2 * theta / (1 - b**2))
    half_life = np.log(2) / theta
    return mu, theta, sigma, half_life