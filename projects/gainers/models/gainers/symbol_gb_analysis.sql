with consolidated as (

    select * from {{ ref('gainers_consolidated') }}

),

aggregated as (

    select
        symbol,
	source,
        count(*) as count,
        avg(price_percent_change) as avg_percent_change,
        sum(price_change) as sum_gross,
        min(file_date) as first_appearance,
        max(file_date) as last_appearance
    from consolidated
    group by symbol

)

select * from aggregated
