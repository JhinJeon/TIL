## 월말평가 오답노트

### 아스키 코드 인덱스

ord() : 문자를 아스키코드 숫자로 반환
chr() : 아스키코드 숫자를 문자로 반환

문제의 코드 :

```python
def caesar(char, n=5):  # char = 입력받은 문장
    new_pw = []  # 암호화된 비밀번호를 반환받을 리스트
    for k in char:  # char의 각 문자를 k로 반환
        encoded = ord(k)+n  # 인코딩 : n만큼 민(더한) 결과를 아스키 코드로 저장
        if encoded > 122:   # 밀어낸 결과가 122(소문자 z)를 벗어나는 경우
            encoded -= 25   # 소문자 a부터 시작하도록 리셋
        elif encoded > 90 and encoded < 97:  # 밀어낸 결과가 90(대문자 Z)을 벗어나는 경우
            encoded -= 25   # 대문자 A부터 시작하도록 리셋
        new_pw.append(chr(encoded))  # chr()로 아스키 코드를 암호화된 문자열로 반환
    answer = ''.join(new_pw)    # 암호화된 결과를 단일 문자열로 반환
    return answer
```

문제점

- n에 26보다 큰 값이 입력됐을 때 알파벳이 아닌 다른 문자를 반환하는 문제가 있음
- (n=5 기준) v, w, x, y, z를 입력 받았을 때(대문자 포함) 원래 출력되어야 하는 문자(a,b,c,d,e)의 한 칸 더 뒤의 값(b,c,d,e,f)을 반환하는 문제가 있음

해결 방안

- 기존 코드의 encoded -= 25 를 encoded -= (n % 26)으로 수정