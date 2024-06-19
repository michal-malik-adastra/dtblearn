{% macro positive_value2(model, column_name) %}
select * from {{ model }} where {{ column_name }} < 1
{% endmacro %}