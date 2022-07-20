## Random

```python
import random
random.choice(list_name)    # list_name에서 단일 값 반환
random.sample(list_name,chrs)
# list_name에서 chrs개 만큼의 값을 무작위로 반환
```

## 줄 바꾸기

1. 따옴표 3개 + Enter

```python
print('''SSAFY
IS
THE BEST''')
```
  - 추가) 작은 따옴표 하나를 감쌀 때는 한 칸 띄우기(' ''')

2. print('txt',sep='\n')

```python
print('SSAFY','IS','THE','BEST',sep='\n')
```
3. for 구문 사용

```python
sentence = ['SSAFY','IS','THE','BEST']
for k in sentence:print(k):
  print(k)
```

4. '\n'.join()

```python
print('\n'.join('SSAFY IS THE BEST'.split()))
```

5. Argument 언패킹

```python
print(*my_list,sep='\n')
```