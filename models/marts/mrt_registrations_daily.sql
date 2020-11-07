with regs as (
    select 
        user_id,
        country,
        created_at
    from {{ ref('fct_registrations') }}
),

final as (
    select
        created_at::date as day,
        country,
        count(*) as reg_count
    from regs
    group by created_at::date, country
)

select * from final
