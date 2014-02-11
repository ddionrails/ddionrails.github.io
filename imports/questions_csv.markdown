---
layout: ddionrails
title: questions.csv
---

question.csv
============

Scales
------

* `txt`: only display the text, no variables are generated. All filters and
  instructions still apply.
* `chr`: result is a character string.
* `int`: result is a integer.
* `dec`: result is a number with decimals.
* `bin`: result is either true, false (equals "null")
* `cat`: result is a pre-defined answer category. See `answers_list` for
  possible answers.

Rules for filter and goto
-------------------------

Filter and goto definitions consist of question names and symbols only,
no keywords (e.g. "goto") are used.

* Symboles `( ) = < > @ | &` -- don't use `>=` or `<=`
* Filter `(AGE > 20) & (SEX = 1)` means: this question is asked if "age" is
  greater than 20 and "sex" is 1
* Goto `(2 @ TARGET)` means: if the answer to the current question is 2 then
  go to question "target"
