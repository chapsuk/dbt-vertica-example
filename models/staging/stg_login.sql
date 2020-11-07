-- try one to one
with source as (
    select * from {{ ref('events_login') }}
),

final as (
    select
        user_id,
        created_at
    from source
)

select * from final
