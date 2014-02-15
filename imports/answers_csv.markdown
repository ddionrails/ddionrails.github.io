---
layout: imports
title: answers.csv
---

answers.csv
===========

* `study` Name of the study (primary key).
* `questionnaire` Name of the questionnaire (primary key).
* `answer_list` Name of the answer_list within the questionnaire (primary key).
* `value` Integer value of the answer (primary key).
* `label` Answer label.

Features
--------

Answer labels are translateable. The language of the translation is set using
a two letter code, e.g. `label_de` for a German label. The default language
for the column `label` is English.
