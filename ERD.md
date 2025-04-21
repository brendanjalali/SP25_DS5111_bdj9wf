## LAB 8 ERD DIAGRAM

```
erDiagram
    WSJGAINERS_NORM ||--o{ GAINERS_CONSOLIDATED : "concatenated"
    YGAINERS_NORM ||--o{ GAINERS_CONSOLIDATED : "concatenated"
    
    WSJGAINERS_NORM {
        string SYMBOL
        float PRICE
        float PRICE_CHANGE
        float PRICE_PERCENT_CHANGE
    }
    
    YGAINERS_NORM {
        string SYMBOL
        float PRICE
        float PRICE_CHANGE
        float PRICE_PERCENT_CHANGE
    }
    
    GAINERS_CONSOLIDATED ||--o{ SYMBOL_GB_ANALYSIS : "Totals by Symbol"
    
    GAINERS_CONSOLIDATED {
        string SYMBOL
        float PRICE
        float PRICE_CHANGE
        float PRICE_PERCENT_CHANGE
        date DATE
        string SOURCE
    }
    
    SYMBOL_GB_ANALYSIS {
        string SYMBOL
        int COUNT
        float AVG_PERCENT_CHANGE
        float SUM_GROSS
        date FIRST_APPEARANCE
        date LAST_APPEARANCE
    }
```
