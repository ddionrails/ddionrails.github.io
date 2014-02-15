---
layout: imports
title: datasets_distributions.csv
---

datasets_distributions.csv
===========

Columns
-------

* `study` Name of the study (primary key).
* `distribution` Name of the distribution (primary key).
* `dataset` Name of the dataset (primary key).
* `version` Versio of the dataset (primary key).

This table builds a has-and-belongs-to-many relationship between datasets
and distributions. Thus, it only consists of key values without any
attributes.
