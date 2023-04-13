import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 238786813 # Ваш chat ID, не меняйте название переменной

def solution(control, test) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    zt = ttest_ind(test, control, alternative='less')
    return zt[1] < 0.01
