with source as (
    select * from {{ ref('events_bro') }}
),

renamed as (
    select
        from_bro as user_from,
        to_bro as user_to,
        created_at
    from source
)

select * from renamed
