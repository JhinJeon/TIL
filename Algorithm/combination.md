## itertools.combinations(a,b)

- a개의 항목들 중 b개를 뽑는 조합
- a는 리스트, b는 정수값으로 입력
  
```python
for chicken in combinations(len(store),m):
    distance = 0
    for h in home:
        distance += abs(h[0] - chicken[0]) + abs(h[1] - chicken[1]) #세로 거리와 가로 거리 더하기
    if distance < maximum:  #최단 거리를 경신하면
        maximum = distance  #최단 거리 대체
print(maximum)
```