Sphinx Bulma Theme
==================

A Sphinx theme based on the `RTD theme <https://github.com/rtfd/sphinx_rtd_theme>`_, built on top of `bulma.io <https://bulma.io>`_.

`Demo <https://sphinx-bulma-theme.readthedocs.io/>`_

.. image:: https://readthedocs.org/projects/sphinx-bulma-theme/badge/?version=latest
   :target: http://sphinx-bulma-theme.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://travis-ci.org/gabrielfalcao/sphinx-bulma-theme.svg?branch=master
    :target: https://travis-ci.org/gabrielfalcao/sphinx-bulma-theme
.. |PyPI python versions| image:: https://img.shields.io/pypi/pyversions/sphinx-bulma-theme.svg
   :target: https://pypi.python.org/pypi/sphinx-bulma-theme
.. |Join the chat at https://gitter.im/gabrielfalcao/sphinx-bulma-theme| image:: https://badges.gitter.im/gabrielfalcao/sphinx-bulma-theme.svg
   :target: https://gitter.im/gabrielfalcao/sphinx-bulma-theme?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Motivation
----------

Bulma has excellent `content markup <https://bulma.io/documentation/elements/content>`_ and great `message boxes <https://bulma.io/documentation/components/message/#colors>`_ for `admonitions <http://docutils.sourceforge.net/docs/ref/rst/directives.html#admonitions>`_

**WORK IN PROGRESS**



Installing
----------

.. code:: bash

   pip install sphinx-bulma-theme


Configuring
-----------

.. code:: python

   import sphinx_bulma_theme

   html_theme = "bulma"
   html_theme_path = [sphinx_bulma_theme.get_html_theme_path()]
   html_theme_options = {
       'logo_path': 'logo.png',  # within _static/
       'admonition_class': 'is-small',
       'analytics_id': None,
       'breadcrumbs_at_top': False,
       'canonical_url': None,
       'collapse_navigation': False,
       'content_margin_left': None,
       'content_padding_left': None,
       'content_padding_top': None,
       'display_version': True,
       'logo_only': False,
       'navigation_depth': 4,
       'prev_next_buttons_location': 'bottom',
       'show_topbar': False,
       'sidebar_class': 'has-text-dark',
       'sidebar_container_class': 'is-one-fifth',
       'sidebar_right': None,
       'theme_sidebar_style': None,
       'topbar_class': 'is-light',
       'topbar_logo_class': 'image is-32x32',
   }


Contributing
------------


.. code:: bash

   pipenv install --dev
   make watch
