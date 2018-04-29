from __future__ import absolute_import

"""Sphinx Bulma theme.

Based on https://github.com/rtfd/sphinx_rtd_theme

"""
from docutils.nodes import warning
from docutils.nodes import tip
from docutils.nodes import Admonition  # noqa
from docutils.nodes import Element  # noqa
from docutils.nodes import compound  # noqa
from docutils.nodes import title
from docutils.nodes import note
from docutils.nodes import section  # noqa
from sphinx.addnodes import seealso
from sphinx.addnodes import toctree  # noqa
from sphinx.addnodes import centered  # noqa
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


def process_admonition_node(node, admonition_type, color, size):
    add_classes_to_node(['message', size, color], node)

    for child in node.traverse(title):
        add_classes_to_node('message-header', child)

    for child in node.traverse(admonition_type):
        add_classes_to_node('message-body', child)
        break


def bulmanize_admonition_nodes(app, doctree, fromdocname):
    theme_options = app.config.html_theme_options
    message_size = theme_options.get('admonition_class', '')

    # size = app.env.conf.get('')
    # nodes = list(filter(lambda n: 'also' in str(n).lower(), doctree.traverse(Element)))
    # for node in nodes:
    #     print(node)
    #     import ipdb; ipdb.set_trace()

    #     atts = dict(node.attlist())
    #     names = " ".join(atts.get('names') or [])
    #     for ad_type, color in admonition_map.items():
    #         ad_name = ad_type.__name__
    #         if ad_name in names:
    #             process_admonition_node(node, ad_type, color)

    for Node, message_color in admonition_map.items():
        for node in doctree.traverse(Node):
            process_admonition_node(node, Node, message_color, message_size)


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
