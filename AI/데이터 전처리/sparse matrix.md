- [성긴 행렬](#성긴-행렬sparse-matrix)
- [NumPy를 이용한 성긴 행렬](#numpy를-이용한-성긴-행렬)
- [np.nonzero](#npnonzero)

# 성긴 행렬(sparse matrix)

- 행렬의 대부분 값이 0인(공백인) 행렬
- 성긴 행렬 방식의 데이터를 처리할 때는 다차원 배열을 통째로 구현하는 것보다 좌표 인덱스와 값만 벡터 형식으로 관리하는 게 효율적이다.

# NumPy를 이용한 성긴 행렬

## np.nonzero(NumPy Array)

- 배열에서 값이 0이 아닌 요소의 인덱스를 반환한다.

```py
import numpy as np

a=np.array([1, 0, 2, 3, 0])
np.nonzero(a)   # array([0, 2, 3])
```

## np.zip(Array A, Array B)

- 동일한 개수로 구성된 자료형을 하나로 묶어준다.

```py
a = np.array([1,3,5,7])
b = np.array([2,4,6,8])

c = np.array(list(zip(a,b)))    # [[1,2],[3,4],[5,6],[7,8]]
```
