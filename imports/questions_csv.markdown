---
layout: ddionrails
title: questions.csv
---

question.csv
============

List of columns
---------------
* `study` String-identifier for the study
* `questionnaire` String-identifier for the questionnaire
* `question` Question number
* `item` Item number
* `number` Question number
* `text` Question text
* `instruction` Interviewer instruction
* `answer_list` Link to list of answers
* `scale` Scale (see list of scales below)
* `filter` Incoming filters (see definition below)
* `goto` Outgoing filters (see definition below)
* `label` Label (DEPRECATED)
* `view_lft` Export only!
* `view_rgt` Export only!
* `view_import_note` Export only!
* `view_import_concept` Export only!
* `view_import_typ` Export only!



Scales
------

* `txt`: only display the text, no variables are generated. All filters and
  instructions still apply.
* `chr`: result is a character string.
* `int`: result is a integer.
* `dec`: result is a number with decimals.
* `bin`: result is either true, false (equals "null")
* `cat`: result is a pre-defined answer category. See `answer_list` for
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
