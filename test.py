#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 zenbook <zenbook@zenbook-XPS>
#
# Distributed under terms of the MIT license.

"""

"""

import ohlc_resampler

import numpy as np
import pandas as pd
from kanichart import StockChart

import os

def main():
    np.random.seed(1)
    data = (np.random.uniform(-0.1, 0.1, 500) + 1).cumprod()
    data = pd.DataFrame(data, index=pd.date_range("2018-01-01", periods=500, freq="T"))
    data = data.resample("5T").ohlc()[0]
    print(data.resample('4H').ohlc2())

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
