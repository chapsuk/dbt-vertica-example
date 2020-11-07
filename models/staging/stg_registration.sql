-- try direct query
select 
    user_id,
    email,
    country,
    ref,
    created_at
from {{ ref('events_registration') }}
