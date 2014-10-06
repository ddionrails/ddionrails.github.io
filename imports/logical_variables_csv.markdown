---
layout: imports
title: logical_variables.csv
---

logical_variables.csv
======================

List of Columns
---------------

* `study` Name of the study (primary key)
* `logical_dataset` Name of the dataset (primary key)
* `logical_variable` Name of the variable (primary key)
* `label` Human-readable label.
* `concept` Name of the underlying concept (foreign key)
* `questionnaire` Name of the underlying questionnaire (foreign key)
* `question` Name of the underlying question (foreign key)
* `item` Name of the underlying item (foreign key)
* `is_primary_key` Boolean indicator, if this variable is part of the
  dataset's primary key.
* `basket_key` Name of an study-specific identifier in this dataset, which
  is used for the script generator.
* `basket_is_default` Boolean indicator, whether a script generator should
  include this variable by default, if its dataset is used.

Special Rules
-------------

* The link to a question (or question item) is only established if the
  question already exists. There are no new questions created by
  variables.csv.
