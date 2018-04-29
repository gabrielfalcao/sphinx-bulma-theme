.. _introduction:


Installing
==========


.. code:: bash

   pip install sphinx-bulma-theme


Configuring
===========

.. code:: python

   import sphinx_bulma_theme

   html_theme = "bulma"
   html_theme_path = [sphinx_bulma_theme.get_html_theme_path()]

   html_theme_options = {
       'logo_path': 'logo.png',
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


.. tip:: Visit the `bulma documentation
         <https://bulma.io/documentation/modifiers/color-helpers/>`_
         to gain better understanding about color and size modifiers
         of the html theme options, such as ``is-small``, ``is-light``, ``has-text-dark``, ``is-one-fifth`` etc
