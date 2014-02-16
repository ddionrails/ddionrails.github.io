---
layout: ddionrails
title: API
---

API
===

<div class="alert alert-warning">
  The DDI on Rails API is still under heavy development.
</div>

Basically, every element in DDI on Rails has an JSON representation. Simply
add `.json` to your URL.

Example:

    get https://[URL]/variables/12       => returns HTML
    get https://[URL]/variables/12.json  => returns JSON

Variable API
------------

    get https://[URL]/api/variable.json?variable=[variable]&study=[study]&dataset=[dataset]

Basket API
----------

    get https://[URL]/api/basket.json?basket=[basket_id]&token=[token]

