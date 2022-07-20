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

## 문자열을 붙여서 출력하려면

1. 숫자(정수, 실수 등) 포맷의 값을 str()로 이용해 문자열로 바꾼 후 +로 붙이기
- 예)
    ```python
    print('종로'+str(3)+'가')
    ```

2. format(f'') 이용하기
- 예)
    ```python
    n = 5
    print(f'남은 시간 : {n}분')
    ```

3. 리스트로 된 값을 붙이는 경우 : ''.join() 이용하기
- 예)
    ```python
    noroo = ['노','루','약','해','요']
    print(''.join(noroo))
    ```

4. print()구문 안에 sep='' 넣기
- 예)
    ```python
    print('서울','대전','대구','부산',sep='')
    ```