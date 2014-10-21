---
layout: imports
title: questions.csv
---

question.csv
============

List of columns
---------------

**(1) Identifier:** The first four columns identify are question. Please note that a question can consist of multiple items. In this case the first item is considered to be the root element and the item is either empty or "root".

Column | Description
-------|------------
`study` | Name of the study (primary key).
`questionnaire` | Name of the questionnaire (primary key).
`question` | Name of the question (primary key).
`item` | Number of the question item (primary key). If the `item` is empty, the question is considered to be a "root question", which might have items.

**(2) Content:** The following columns represent the content of a question or item

Column | Description
-------|------------
`number` | Question number (integer), as a reference to the position in the questionnaire.
`text` | Question text.
`instruction` | Interviewer instruction.
`answer_list` | Name of the list of answers (foreign key). The `answers.csv`.
`scale` | Scale (see list of scales below) of the answers.
`filter` | Incoming filters (see definition below).
`goto` | Outgoing filters (see definition below).
`label` | Label (DEPRECATED).
`description` | Human readable description including additional unstructured information.
`concept` | Name of question's concept (foreign key). In DDI on Rails the primary link from a question to one or multiple concepts is through the question's logical variables. Nevertheless, it is possible to link a question or an item directly to a concept.

**(3) Links to logical variables and concepts (import only):** A question can be linked to multiple logical variables. Therefore, DDI on Rails stores this link with the logical variables. Yet, the questions import allows to link every question to one logical variable.

Column | Description
-------|------------
`logical_dataset` | Logical dataset name (foreign key).
`logical_variable` | Logical variable name (foreign key).

**(4) Export only:** There is a couple of columns that is included in the export but will not be imported.

Column | Description
-------|------------
`view_sort_id` | Sort order of the questions. The `view_sort_id` is generated from the order of the questions in the import file.
`view_lft` | and `view_rgt` Export only.
`view_import_note` | Export only (DEPRECATED).
`view_first_concept` | Concept of the question, based on the first related variable.
`view_import_typ` | Export only (DEPRECATED).
`view_calculated_number` and `view_calculated_item` | Special information for imports following the SOEP-QLIB-conventions.
`logical_variable` | Name of the resulting variable (foreign key, import only).
`logical_dataset` | Name of the dataset of the resulting variable (foreign key, import only).

**(5) Namespaces (neither imported nor exported):** Every study can add an arbitrary number of columns to store additional information that are not intended to be imported in DDI on Rails. Those columns are prefixed with `internal_`


Scales
------

Code | Meaning
-----|--------
`txt` | Only display the text, no variables are generated. All filters and instructions still apply.
`chr` | Result is a character string.
`int` | Result is a integer.
`dec` | Result is a number with decimals.
`bin` | Result is either true, false (equals "null")
`cat` | Result is a pre-defined answer category. See `answer_list` for possible answers.

Rules for filter and goto
-------------------------

Filter and goto definitions consist of question names and symbols only,
no keywords (e.g. "goto") are used.

* Symboles `( ) = < > @ | & : != <= >=`
* Filter `(AGE > 20) & (SEX = 1)` means: this question is asked if "age" is
  greater than 20 and "sex" is 1
* Goto `(2 @ TARGET)` means: if the answer to the current question is 2 then
  go to question "target"
* Refer to items using the colon as a seperator, e.g. `(PSOR:2 = 3)`.
* Value lists and ranges: `(x = 1:3)` is equal to `(x = 1,2,3)` is equal to `(x = 1) | (x = 2) | (x = 3)`
