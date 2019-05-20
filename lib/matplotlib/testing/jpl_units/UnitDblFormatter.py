"""UnitDblFormatter module containing class UnitDblFormatter."""

import matplotlib.ticker as ticker

__all__ = ['UnitDblFormatter']


class UnitDblFormatter(ticker.ScalarFormatter):
    """The formatter for UnitDbl data types.  This allows for formatting
        with the unit string.
    """
    def __init__(self, *args, **kwargs):
        'The arguments are identical to matplotlib.ticker.ScalarFormatter.'
        ticker.ScalarFormatter.__init__(self, *args, **kwargs)

    def __call__(self, x, pos=None):
        'Return the format for tick val x at position pos'
        if len(self.locs) == 0:
            return ''
        else:
            return f'{x:.12}'

    def format_data_short(self, value):
        "Return the value formatted in 'short' format."
        return f'{value:.12}'

    def format_data(self, value):
        "Return the value formatted into a string."
        return f'{value:.12}'
