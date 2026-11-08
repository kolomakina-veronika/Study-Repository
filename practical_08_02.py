consumption = [6, 12, 2, 4, 3, 9, 2, 8, 3, 4, 5, 3]
limit = 15
p = [0]
for x in consumption:
    p.append(p[-1] + x)
queries = [(0, 2), (3, 5), (6, 8), (9, 11)]
for l, r in queries:
    t = p[r + 1] - p[l]
    status = "ПЕРЕВИЩЕННЯ" if t > limit else "норма"
    print(f"години {l}-{r}: {t} кВт·год, {status}")