with bros as (
    select 
        user_from,
        user_to,
        created_at
    from {{ ref('stg_bro') }}
),

renamed as (
    select
        user_from as actor_id,
        user_to as receiver_id,
        created_at
    from bros
)

select * from renamed
