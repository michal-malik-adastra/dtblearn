{{
    config(
        materialized = 'incremental',
        on_schema_change = 'fail',
        tags=[var('tag_fct')]
    )
}}
select {{ dbt_utils.generate_surrogate_key(['listing_id', 'review_date', 'reviewer_name', 'review_text']) }} review_id, *
from {{ref('src_reviews')}}
where review_text is not null
{% if is_incremental() %}
    {% if var("start_date", false) and var("end_date", false) %}
        {{ log("Loading " ~ this ~ ' incrementally (start_date: ' ~ var("start_date") ~ ', end_date: ' ~ var("end_date") ~ ')', info=true)}}
        and review_date >= '{{ var("start_date") }}'
        and review_date < '{{ var("end_date") }}'
    {% else %}
        {{ log('Loading ' ~ this ~ ' incrementally (all missing dates)', info=True)}}
        and review_date > (select max(review_date) from {{this}})
    {% endif %}
{% endif %}