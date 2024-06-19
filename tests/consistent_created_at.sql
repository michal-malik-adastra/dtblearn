{{
    config=(
        tags=[var('tag_test')]
    )
}}
select f.listing_id, f.reviewer_name, f.review_date, d.created_at
from {{ ref('fct_reviews') }} f
join {{ ref('dim_listings_cleansed') }} d on f.listing_id = d.listing_id
where f.review_date <= d.created_at