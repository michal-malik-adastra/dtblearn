select is_full_moon, review_sentiment, count(*) as reviews
from {{ ref('mart_fullmoon_review') }}
group by is_full_moon, review_sentiment
order by is_full_moon, review_sentiment