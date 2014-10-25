---
layout: imports
title: studies.csv
---

studies.csv
===========

Columns
-------

Column | Description
-------|------------
`organization` | Name of the organization (foreign key)
`study` | Name of the study (primary key).
`label` | Human-readable label.
`description` | Description (using Markdown).
`html_description` | HTML description (DEPRECATED).
`language_string` | Whitespace seperated list of languages used in the study as two-figure language codes (e.g. "de en"). These parameters are used to import and export the translations of questionnaires and datasets.
`import_url` | URL from where all import files are retrieved.
`files_url` | URL from where files are loaded interactively.
`import_config` | Addintional import parameters, currently not used.
