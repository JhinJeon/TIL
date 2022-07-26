## random 함수 이용하기

- 외부에서 불러오기 필요(import random) 입력

```python
import random
```

## random.choice(integers)

- integers들 중에서 임의의 값 하나를 반환
- random.choice()안에 리스트를 넣으면 리스트의 값들 중에서 무작위 값 반환

## random.sample(integers, n)

- integers들 중에서 n개의 값을 무작위로 반환


```python
import random
random.choice(list_name)    # list_name에서 단일 값 반환
random.sample(list_name,num)
# list_name에서 num개 만큼의 값을 무작위로 반환
```
