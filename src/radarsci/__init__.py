"""
RadarSci: a radar for scientific literature.
"""

from importlib.metadata import version, PackageNotFoundError


try:  # pragma: no cover - metadata discovery
    __version__ = version("radarsci")
except PackageNotFoundError:  # pragma: no cover - local execution
    __version__ = "0.0.0"


__all__ = ["__version__"]
