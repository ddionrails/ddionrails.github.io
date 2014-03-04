---
layout: imports
title: questions.csv
---

question.csv
============

List of columns
---------------
* `study` Name of the study (primary key).
* `questionnaire` Name of the questionnaire (primary key).
* `question` Name of the question (primary key).
* `item` Number of the question item (primary key). If the `item` is empty,
  the question is considered to be a "root question", which might have items.
* `number` Question number, as found in the questionnaire.
* `concept` Name of question's concept (foreign key).
* `text` Question text.
* `instruction` Interviewer instruction.
* `answer_list` Name of the list of answers (foreign key).
* `scale` Scale (see list of scales below) of the answers.
* `filter` Incoming filters (see definition below).
* `goto` Outgoing filters (see definition below).
* `label` Label (DEPRECATED).
* `view_sort_id` Sort order of the questions. The `view_sort_id` is generated
  from the order of the questions in the import file.
* `view_lft` and `view_rgt` Export only.
* `view_import_note` Export only (DEPRECATED).
* `view_first_concept` Concept of the question, based on the first related
  variable.
* `view_import_typ` Export only (DEPRECATED).
* `view_calculated_number` and `view_calculated_item` Special information for
  imports following the SOEP-QLIB-conventions.

Scales
------

* `txt` Only display the text, no variables are generated. All filters and
  instructions still apply.
* `chr` Result is a character string.
* `int` Result is a integer.
* `dec` Result is a number with decimals.
* `bin` Result is either true, false (equals "null")
* `cat` Result is a pre-defined answer category. See `answer_list` for
  possible answers.

Rules for filter and goto
-------------------------

Filter and goto definitions consist of question names and symbols only,
no keywords (e.g. "goto") are used.

* Symboles `( ) = < > @ | & :` -- don't use `>=` or `<=`
* Filter `(AGE > 20) & (SEX = 1)` means: this question is asked if "age" is
  greater than 20 and "sex" is 1
* Goto `(2 @ TARGET)` means: if the answer to the current question is 2 then
  go to question "target"
* Refer to items using the colon as a seperator, e.g. `(PSOR:2 = 3)`.
