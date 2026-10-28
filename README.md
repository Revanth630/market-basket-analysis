# Market Basket Analysis

Association-rule mining that finds products customers buy together. This is the analysis I ran in proof-of-concept work at NanoBi Analytics.

## Method
- Convert each transaction into a one-hot basket matrix (pandas)
- Count frequent item pairs above a minimum **support**
- Calculate **confidence** and **lift** in both directions and rank rules by lift

## Business use
High-lift rules (for example *tea → sugar, biscuits*) drive cross-sell bundles, shelf placement and combo offers.

## Run
```bash
pip install -r requirements.txt
python market_basket.py
```
> The transactions are synthetic. The implementation is pure pandas, with no black-box library.
