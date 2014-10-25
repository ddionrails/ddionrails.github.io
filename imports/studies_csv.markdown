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
`import_url` | URL from where all import files are retrieved.
`files_url` | URL from where files are loaded interactively.
`import_config` | Addintional import parameters, currently not used.
