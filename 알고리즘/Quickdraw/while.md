## 함수 안에 while문을 쓸 때

- while 반복문의 종료 조건으로 True:를 설정하면 함수에서 False 반환 시 반복문 종료

```python
def rotate(k=):
  while True:
    k += 1
    print(k)
    if k >= 5:
      return False
    if k == 12:
      break

print(rotate(0))  
# 결과 : 
# 1
# 2
# 3
# 4
# 5 
# False
```