=========================
collective.behavior.price
=========================

collective.behavior.price provides price related behavior to dexterity content types.

Currently Tested with
---------------------

* Plone-4.2.2 [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.price.interfaces.IPrice" />
    ...
  </property>

You may also set currency through content registry and content price with currency will be also cataloged with metadata called ``money``.

Farther Documentation URL
-------------------------

`http://packages.python.org/collective.behavior.price/
<http://packages.python.org/collective.behavior.price/>`_

Repository URL
--------------

`https://github.com/collective/collective.behavior.price/
<https://github.com/collective/collective.behavior.price/>`_
