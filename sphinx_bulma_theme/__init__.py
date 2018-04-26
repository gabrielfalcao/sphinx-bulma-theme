from __future__ import absolute_import

"""Sphinx Bulma theme.

Based on https://github.com/rtfd/sphinx_rtd_theme

"""
from .fs import module_path
from .version import version


def get_html_theme_path():
    """Return list of HTML theme paths."""
    return str(module_path)


def setup(app):
    app.add_html_theme('bulma', get_html_theme_path())
    # # DEBUG
    # import ipdb; ipdb.set_trace()


__all__ = (
    'get_html_theme_path',
    'version',
    'setup',
)
