# 0. 기본

## print(end=)

- end의 기본 값은 줄 바꿈 ('\n')
- end= 입력 시 print되는 값 맨 뒤에 입력한 값이 출력됨

## print(sep=)

- sep의 기본 값은 공백(' ')
- sep= 입력 시 콤마로 구분된 print 값 사이에 입력한 값이 출력됨

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
5. 정수 값이 담긴 리스트를 출력하는 경우
- 예)
    ```python
    t = int(input())

    li = [2, 3, 5, 7, 11]

    for tc in range(1, t + 1):
        n = int(input())
        answer = [0] * 5
        for i in range(5):
            while n % li[i] == 0:
                answer[i] += 1
                n //= li[i]

        print(f'#{tc}', end=' ')
        print(*answer)
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

## 리스트의 인덱스와 값을 같이 뽑기

- 1.range(클래식)

```python
a = ['a','b','c','d','e','f','u']
for i in range(a):
    print(i,a[i])
```

- 2.enumerate

```python
a = ['a','b','c','d','e','f','u']
for idx,val in enumerate(a):
    print(idx,val)
```