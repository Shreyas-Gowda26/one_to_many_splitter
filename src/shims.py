from typing import Tuple

try:
    # Asserting optional dependencies exist
    np = __import__('numpy')
    np.divmod
    # Defining wrappers
    def divmod(x: int, y: int) -> Tuple[int, int]:
        out = np.divmod(x, y)
        return int(out[0]), int(out[1])
except (AttributeError, ModuleNotFoundError):
    # Defining custom wrappers
    def divmod(x: int, y: int) -> Tuple[int, int]:
        return __builtins__.divmod(x, y)
