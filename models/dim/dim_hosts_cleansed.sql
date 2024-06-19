{{
    config(
        materialized = 'view',
        tags=[var('tag_dim')]
    )
}}
select id_host host_id, ifnull(host_name, 'Anonymous') host_name, is_superhost, created_at, updated_at
from {{ref('src_hosts')}}