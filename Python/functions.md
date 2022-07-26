## enumerate

- enumerate(list)는 list에서 인덱스와 값을 각각 튜플 형태로 반환한다.

```python
sample = [1,3,5,7,9]
for index,value in enumerate(sample):
    print(index,value)
```
- 위 코드에서 index는 sample 리스트의 인덱스(왼쪽에서 몇 번째인지), value는 리스트 인덱스에 저장된 값을 반환한다.

```python
word = 'abcdefghijklmnop'
for i, letter in enumerate(word):
    if i > 0 and i % 6 == 0:
        print()
    print(letter,end='')
#6개 문자를 출력할 때 마다 print()를 출력하여 줄바꾸기를 한 후 end=''로 공백과 문자들을 모두 붙여서 출력
```

enumerate를 응용하면 문자열 n개마다 줄을 바꾸어서 출력할 수 있다.

---