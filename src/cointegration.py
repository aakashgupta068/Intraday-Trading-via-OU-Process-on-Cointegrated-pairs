from statsmodels.tsa.vector_ar.vecm import coint_johansen
from statsmodels.tsa.stattools import adfuller

def get_cointegration_vector(data, det_order=-1, k_ar_diff=1):
    result = coint_johansen(data, det_order=det_order, k_ar_diff=k_ar_diff)
    beta = result.evec[:, 0] / result.evec[0, 0]
    return beta

def adf_test(series):
    return adfuller(series.dropna())[1]  # Return p-value