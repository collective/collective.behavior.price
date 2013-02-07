=========================
collective.behavior.price
=========================

collective.behavior.price provides price related behavior to dexterity content types.

Currently tested with
---------------------

* Plone-4.2.4 [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.price.interfaces.IPrice" />
    ...
  </property>

You may also set currency through content registry and content price with currency will be also cataloged with metadata called ``money``.
