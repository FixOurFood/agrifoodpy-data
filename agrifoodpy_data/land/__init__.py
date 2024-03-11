"""Food module"""

import os
import xarray as xr

available = [
    "ALC_500",
    "ALC_1000",
    "ALC_2000",
    "ALC_5000",
    "CEH_5000",
    "UKCEH_LC_1000",
    "UKCEH_LCPCP_1000",
    "UKCEH_LCPCP_2000",
    "UKCEH_LCPCP_5000",
             ]

data_dir = os.path.join(os.path.dirname(__file__), 'data/' )

def __getattr__(name):
    if name not in available:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}.")

    _data_file = f'{data_dir}{name}.nc'

    # If the file contains more than a single dataarray, then it will try
    # to load it as a dataset
    try:
        with xr.open_dataset(_data_file) as data:
            data.load()
            return data
        
    except ValueError:
        with xr.open_dataarray(_data_file) as data:
            data.load()
            return data
