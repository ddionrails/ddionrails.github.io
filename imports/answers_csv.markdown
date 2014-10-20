---
layout: imports
title: answers.csv
---

answers.csv
===========

## List of columns

**(1) Identifiers:** The first three columns identify an answer list. An answer list always refers to one questionnaire. It is not possible to refere from a question in questionnaire A to an answer list in questionnaire B.

The fourth column (`value`) identifies an item of an answer list.

* `study` Name of the study (primary key).
* `questionnaire` Name of the questionnaire (primary key).
* `answer_list` Name of the answer_list within the questionnaire (primary key).
* `value` Integer value of the answer (primary key).

**(2) Content:** The content of an item is a label. This label can be translated.

* `label` Answer label in the primary language (usualy English).
* `label_*` Translations of the label. Please replace `*` by a two-digit language code, e.g. `label_de` for a German label.

## Features

Answer labels are translateable. The language of the translation is set using
a two letter code, e.g. `label_de` for a German label. The default language
for the column `label` is English.
