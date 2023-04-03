## \U 출력하려 할 때 유니코드 에러가 발생하는 경우

- 유니코드 에러 : 문자열 출력 과정에서 \u 또는 \U 입력 시 unicodeerror 발생할 수 있음
   - 만약 문자열 앞에 r을 붙이지 않으면 다음과 같은 에러가 발생한다:
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 51-52: truncated \UXXXXXXXX escape

## 해결 방안

- 프로그램 경로를 입력할 때처럼 \u가 들어가는 문자열을 출력하려면 앞에 r을 붙여야 함

## 느낀 점

- 문자열 안에 큰 따옴표(또는 작은 따옴표)를 출력할 때는 감싸는 큰 따옴표(작은 따옴표)가 잘 처리되어 있는지 다시 한 번 확인해야 한다.

```python
print(r'”파일은 c:\Windows\Users\내문서\Python에 저장이 되었습니다.”',
"나는 생각했다. ‘cd를 써서 git bash로 들어가 봐야지.’",
sep = '\n')
```