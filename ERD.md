## LAB 8 ERD DIAGRAM
This report presents the intermediate tables that allow for analysis of the combined data from wsjgainers and ygainers

### Use Cases:
#### Gainers Consolidated:
Gainers Consolidated allows for the combination of both raw table sources of the normalized wsjgainers and the ygainers. 
#### Symbol Groupby Analysis:
This groupby table allows for aggregation by symbol and allows a comparison of occurences, average percent change, and total gross change by corresponding symbol

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

### Methods:
The data was processed by concatenating the normalized tables and adding symbol and date fields to identify when and where the rows came from. From there, a grouped by table was created to get a look into the trends by symbol.

### Summary:
There are other suplimentary tables that could provdide further insight into the trends of the data but this is a start. The data generated does prove useful for our goal of understanding the gainers over time.
