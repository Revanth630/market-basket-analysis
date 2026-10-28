"""Market basket analysis: frequent item pairs and association rules (support, confidence, lift) in pandas."""
from itertools import combinations

import numpy as np
import pandas as pd

RNG = np.random.default_rng(3)
ITEMS = ["bread", "milk", "eggs", "butter", "tea", "sugar", "biscuits", "rice", "dal", "oil"]
BUNDLES = [["bread", "butter"], ["tea", "sugar", "biscuits"], ["rice", "dal", "oil"], ["milk", "eggs"]]


def make_baskets(n=3000):
    baskets = []
    for _ in range(n):
        basket = set(RNG.choice(ITEMS, RNG.integers(1, 4), replace=False))
        for b in BUNDLES:
            if RNG.random() < 0.25:
                basket.update(b)
        baskets.append(sorted(basket))
    return baskets


def association_rules(baskets, min_support=0.05):
    n = len(baskets)
    onehot = pd.DataFrame([{i: 1 for i in b} for b in baskets]).fillna(0).astype(bool)
    support = onehot.mean()
    rules = []
    for a, b in combinations(onehot.columns, 2):
        s_ab = (onehot[a] & onehot[b]).sum() / n
        if s_ab < min_support:
            continue
        for x, y in ((a, b), (b, a)):
            conf = s_ab / support[x]
            rules.append({"antecedent": x, "consequent": y, "support": s_ab,
                          "confidence": conf, "lift": conf / support[y]})
    return pd.DataFrame(rules).sort_values("lift", ascending=False)


if __name__ == "__main__":
    rules = association_rules(make_baskets())
    print(rules.head(10).round(3).to_string(index=False))
