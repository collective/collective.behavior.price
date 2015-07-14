=========================
collective.behavior.price
=========================

collective.behavior.price provides price related behavior to dexterity content types.

.. image:: https://secure.travis-ci.org/collective/collective.behavior.price.png
    :target: http://travis-ci.org/collective/collective.behavior.price

Currently tested with
---------------------

* Plone-4.3.6 with Python-2.7.10 [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.price.interfaces.IPrice" />
    ...
  </property>

You may also set currency through content registry and price with currency will be also cataloged with metadata: ``money``.
