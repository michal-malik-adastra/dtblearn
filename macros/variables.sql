{% macro learn_variables() %}
{% set your_name_jinja = "Michal" %}
{{ log("Hello: " ~ your_name_jinja, info=True) }}
{{ log("Hello dbt user: " ~ var("user_name", "default"), info=True)}}
{{ log("Hi from dbt_project.yaml: " ~ var("user_name_dbt_project_yml"), info=True)}}
{{ log("Hi from dbt_project.yaml (overwrite): " ~ var("user_name_dbt_project_yml", "yml overwrites default in func"), info=True)}}
{% endmacro %}