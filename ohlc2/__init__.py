"""ohlc2 - ohlc resampler"""

__version__ = '0.1.0'
__author__ = 'fx-kirin <ono.kirin@gmail.com>'
__all__ = []

from pandas.core import resample

def ohlc2(self, *args, **kwargs):
    """`pd.DataFrame.resample(<TimeFrame>).ohlc2()`
    Resample method converting OHLC to OHLC
    """
    cdict = dict([(v.lower(), v) for v in self.asfreq().columns])
    try:
        agdict = {cdict['open']: 'first',
                  cdict['high']: 'max',
                  cdict['low']: 'min',
                  cdict['close']: 'last'}
    except KeyError as e:
        raise KeyError('Columns not enough {}'.format(*e.args))
    if 'volume' in map(lambda x: x.lower(), self.asfreq().columns):
        agdict[cdict['volume']] = 'sum'
    return self.agg(agdict)


# Add instance as `pd.DataFrame.resample('<TimeFrame>').ohlc2()`
resample.DatetimeIndexResampler.ohlc2 = ohlc2
