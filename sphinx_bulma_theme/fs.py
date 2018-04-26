# -*- coding: utf-8 -*-

try:
    from pathlib2 import Path
except ImportError:
    from pathlib import Path


module_path = Path(__file__).parent


__all__ = (
    'module_path',
)
