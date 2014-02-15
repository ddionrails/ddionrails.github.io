---
layout: imports
title: topics.csv
---

topics.csv
===========

Columns
-------

* `topic` Name of the topic (primary key).
* `parent` Name of the parent topic (foreign key). If empty, this topic
  becomes a root-level topic, requiring an icon.
* `label` Short label.
* `description` Description using Markdown.
