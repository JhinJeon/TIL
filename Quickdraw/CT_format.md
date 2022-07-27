# 1. 문자열을 붙여서 출력하려면

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

---
## 문자열을 줄울 바꿔서 출력하려면
1. print() 안에 sep = '\n' 넣기
- 예)
    ```python
    print('서울','대전','대구','부산',sep'\n')
    ```
2. for문 이용하기
- 예)
    ```python
    taste = ['민초','파피','부먹','진순']
    for t in taste:
        print(t)
    ```

3. 따옴표 3개 + Enter

```python
print('''SSAFY
IS
THE BEST''')
```
- 추가) 작은 따옴표 하나를 감쌀 때는 한 칸 띄우기(' ''')

4. '\n'.join()

```python
print('\n'.join('SSAFY IS THE BEST'.split()))
```

5. Argument 언패킹

```python
print(*my_list,sep='\n')
```