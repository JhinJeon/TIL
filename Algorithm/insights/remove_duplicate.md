## 연속되는 문자열 제거하는 코드(다른 아이디어)

```python
numbers = [1, 1, 2, 4, 5, 5, 13, 3, 3, 0, 1, 1]

idx = []  # 중복되는 숫자가 들어간 인덱스 리스트
for i in range(len(numbers) - 1):
  # 기준 값과 비교하려는 값이 같으면 idx 리스트에 추가
  if numbers[i] == numbers[i + 1]:
    idx.append(i)

for j in range(len(idx)):
  # idx 리스트에서 인덱스 번호를 조회해서 numbers 리스트에서 해당 값 pop
  numbers.pop(idx[j])
  # 인덱스 범위를 벗어나지 않도록 idx에 저장된 모든 인덱스 값을 1씩 빼기
  for m in range(len(idx)):
    idx[m] -= 1


print(numbers)
```