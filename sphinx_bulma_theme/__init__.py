from __future__ import absolute_import

"""Sphinx Bulma theme.

Based on https://github.com/rtfd/sphinx_rtd_theme

"""
from docutils.nodes import warning
from docutils.nodes import tip
from docutils.nodes import note
from sphinx.addnodes import seealso
from sphinx.addnodes import toctree
# from sphinx.addnodes import centered
from six import string_types
from .fs import module_path
from .version import version

admonition_map = {
    seealso: 'is-info',
    tip: 'is-primary',
    note: 'is-warning',
    warning: 'is-danger',
}


def get_html_theme_path():
    """Return list of HTML theme paths."""
    return str(module_path)


def add_classes_to_node(class_names, node):
    if isinstance(class_names, string_types):
        class_names = class_names.split()

    return list(map(node.set_class, class_names))


def process_admonition_node(node, color):
    add_classes_to_node(['box', 'message', color], node)
    for child in node.children:
        add_classes_to_node('message-body', child)


def bulmanize_admonition_nodes(app, doctree, fromdocname):
    # for node in doctree.traverse(toctree):
    #     import ipdb; ipdb.set_trace()

    for Node, color in admonition_map.items():
        for node in doctree.traverse(Node):
            process_admonition_node(node, color)


def handle_page_context(app, pagename, templatename, context, doctree):
    pass


def setup(app):
    app.add_html_theme('bulma', get_html_theme_path())
    app.connect('doctree-resolved', bulmanize_admonition_nodes)
    app.connect('html-page-context', handle_page_context)


__all__ = (
    'get_html_theme_path',
    'version',
    'setup',
    'admonition_map',
)
