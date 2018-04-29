.. _html theme options:

Theme Options
=============



------

.. _option default_admonition_class:

**default_admonition_class**

Defaut color of admonitions

**type:** :py:class:`str`
**default:** ``is-light``

------

.. _option breadcrumbs_at_top:

**breadcrumbs_at_top**

Whether to shop breadcrumbs on the top of the page.


**type:** :py:class:`bool`
**default:** ``False``

------

.. _option canonical_url:

**canonical_url**

Force all internal links to use this value as base url

**type:** :py:class:`str`
**default:** ``None``


------

.. _option collapse_navigation:

**collapse_navigation**

**type:** :py:class:`bool`
**default:** ``False``

------

.. _option content_margin_left:

**content_margin_left**

**type:** :py:class:`str`
**default:** ``None``
**example:** ``20px``

------

.. _option content_padding_left:

**content_padding_left**

**type:** :py:class:`str`
**default:** ``None``
**example:** ``20px``

------

.. _option content_padding_top:

**content_padding_top**

If set to ``None`` the theme will determine the best default depending on whether the :ref:`topbar is visible <option show_topbar>`
**type:** :py:class:`str`
**default:** ``None``
**example:** ``20px``

------

.. _option display_version:

**display_version**

**type:** :py:class:`bool`
**default:** ``True``

------

.. _option logo_only:

**logo_only**

Define a :ref:`logo_path <option logo_path>` and set this to ``True``
if you want to omit your project title and only show the logo.

**type:** :py:class:`bool`
**default:** ``False``


------

.. _option logo_path:

**logo_path**

Relative path to your project's ``source/_static``

**type:** :py:class:`str`
**default:** ``None``
**example:** ``my-project-name.png``


------

.. _option navigation_depth:

**navigation_depth**

The maximum depth of the toctree

**type:** :py:class:`int`
**default:** ``6``


------

.. _option show_topbar:

**show_topbar**

Whether to show topbar or sidebar

**type:** :py:class:`bool`
**default:** ``False``

------

.. _option sidebar_class:

**sidebar_class**

Sets the color of project title on sidebar

**type:** :py:class:`str`
**default:** ``has-text-dark``
**example:** ``my-project-name.png``


------

.. _option sidebar_container_class:

**sidebar_container_class**

Sets the width of the sidebar

**type:** :py:class:`str`
**default:** ``is-3``

------

.. _option sidebar_right:

**sidebar_right**

Whether to show sidebar on the right side of the page

**type:** :py:class:`bool`
**default:** ``False``

------

.. _option sidebar_style:

**theme_sidebar_style**

Defines the inline CSS rules for the sidebar. The theme will determine
the best margin for the sidebar by default but you can customize it
here.


**type:** :py:class:`str`
**default:** ``None``
**example:** ``margin: 32px``

------

.. _option topbar_class:

**topbar_class**

**type:** :py:class:`str`
**default:** ``is-light``


------

.. _option topbar_logo_class:

**topbar_logo_class**

**type:** :py:class:`str`
**default:** ``image is-32x32``
