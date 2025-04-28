-- models/gainers/gainers_consolidated.sql

with wsj as (

    select
        symbol,
        price,
        price_change,
        price_percent_change,
        'wsj' as source,
        current_date as file_date
    from {{ ref('wsjgainers_norm20250406_215103') }}

),

yahoo as (

    select
        symbol,
        price,
        price_change,
        price_percent_change,
        'yahoo' as source,
        current_date as file_date
    from {{ ref('ygainers_norm20250406_215048') }}

)

select * from wsj
union all
select * from yahoo
