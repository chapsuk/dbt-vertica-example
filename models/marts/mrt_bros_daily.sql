with bros as (
    select * from {{ ref('fct_bros') }}
),

regs as (
    select * from {{ ref('fct_registrations') }}
),

final as (
    select
        b.created_at::date as day,
        r.country as country,
        count(*) as bros_count
    from bros as b
    left join regs as r on b.actor_id = r.user_id
    group by b.created_at::date, r.country
)

select * from final
