## set에서 에러 내지 않고 값 지우기

- .discard() 이용

```python
my_set = {'민트', '초코', '피자'}
my_set.discard('민트')
print(my_set)  # {'초코','피자'}
```