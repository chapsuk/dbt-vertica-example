select user_id, country, created_at from {{ ref('stg_registration') }}
