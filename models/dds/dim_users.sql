with users as (
    select user_id, email from {{ ref('stg_registration') }}
),

final as (
    select
        user_id as id,
        email
    from users
)

select * from final