import importlib.util
import os

import numpy as np

import shims

_SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
_SHIMS_NAME = 'shims'
_SHIMS_PATH = os.path.join(_SCRIPT_DIR, f'{_SHIMS_NAME}.py')

def test_divmod_native() -> None:
    '''Tests divmod with numpy support'''
    assert np.divmod is not None
    assert shims.divmod(16, 5) == (3, 1), 'divmod with numpy failed'

def test_divmod_shim() -> None:
    '''Tests divmod without numpy support'''
    spec = importlib.util.spec_from_file_location(_SHIMS_NAME, _SHIMS_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    exec(
'''
import sys

import pytest

# Disabling numpy support
sys.modules['numpy'] = None
with pytest.raises(ModuleNotFoundError):
    __import__('numpy')

# Loading module
spec.loader.exec_module(module)
shims = sys.modules['shims']
assert shims.divmod(16, 5) == (3, 1), 'divmod shim failed'
''',
        {},
        {
            'spec': spec,
            'module': module
        }
    )
