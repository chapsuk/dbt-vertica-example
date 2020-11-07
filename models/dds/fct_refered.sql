with refered as (
    select 
        user_id,
        ref,
        created_at
    from {{ ref('stg_registration') }}
),

final as (
    select
        {{ dbt_utils.get_url_parameter('ref', 'bro') }} as actor_id,
        user_id as target_id,
        created_at
    from refered
    where ref is not null
)

select * from final
