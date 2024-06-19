select id id_host, name host_name, is_superhost, created_at, updated_at
from {{source('airbnb', 'hosts')}}