import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 238786813 # Ваш chat ID, не меняйте название переменной

def solution(control, test) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    zt = ztest(test, value = control.mean(), alternative='smaller')
    return zt[1] < 0.01
