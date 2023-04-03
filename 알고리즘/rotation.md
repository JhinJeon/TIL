## 이차원 배열 회전 알고리즘

- 리스트로 만들어진 이차원 배열을 왼쪽 또는 오른쪽으로 90도 회전한다고 가정했을 때 배열 값의 위치는 일정한 규칙에 따라 변한다.

- n * n의 배열에서 회전하기 전 원래 값의 인덱스를 graph[i][j]로 가정한다면,
    - 왼쪽으로 90도 회전했을 때 graph[i][j]에 있던 값은 graph[n-j+1][i]의 위치로 이동한다.
    - 오른쪽으로 90도 회전했을 때 graph[i][j]에 있던 값은 graph[j][n-i+1]의 위치로 이동한다.

참고 자료 : 

<https://shoark7.github.io/programming/algorithm/rotate-2d-array>




관련 문제 :

<https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=2001&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1> - 큰 사각형 안에서 작은 사각형 범위 안의 값을 계산할 때 인덱스 범위가 벗어나거나 그래프 전체를 포괄하지 못하는 불상사가 발생하지 않아야 한다.
- 또한 이차원 리스트 안에 있던 값들을 저장해야 할 떄는, for 구문의 줄 위치를 잘 봐서 잘못된 값이 나오지 않도록 주의해야 한다.
  
---