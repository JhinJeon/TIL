# 이차원 행렬로 전환하기

- pandas의 pivot_table 이용
- pd.pivot_table(pd.Dataframe() 소스, index=[행 데이터], columns=[열 데이터], value=[값 데이터], fill_value=빈 행에 채울 값)
  - index에 여러 행을 입력하면 여러 행들을 기준으로 데이터가 전환된다.

```py
# pivot_table은 pandas에서 지원하는 DataFrame 형식의 데이터를 활용해야 함
import pandas as pd

df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})

table = pd.pivot_table(df, values='D', index=['A', 'B'],
                    columns=['C'], aggfunc=np.sum)

# table에 저장된 데이터
table
C        large  small
A   B
bar one    4.0    5.0
    two    7.0    6.0
foo one    4.0    1.0
    two    NaN    6.0
```

# 행렬 간 곱셈

- 두 행렬 간 곱셈은 (열 데이터 \* 행 데이터의 합) 이다.
- 행렬곱을 진행하려면 첫째 행렬의 열 개수와 둘째 행렬의 행 개수가 같아야 한다.
  - (n \* m) 행렬과 (m \* p) 행렬은 첫째 행렬의 열 개수와 둘째 행렬의 행 개수가 같으므로(m) 행렬곱이 가능하다.

# pd.DataFrame 전처리

- df는 pd.DataFrame으로 전환된 데이터프레임

## 상위 n개 표시

- df.head(n)

## 모든 항목 개수 세기

- df\[column].count()

## 특정 항목의 평균 구하기

- df_avg = df.groupby(\[column], as_index=False).mean()
- 항목별로 그룹을 이루고 싶을 때 groupby(\[column])을 이용해 묶을 수 있다.

## 각 항목의 평균값 표시

```py
# x에는 x축에 표시할 범주, height에는 y축에 표시할 값 입력
chart = plt.bar(x=data_avg[column1], height=data_avg[column2])
plt.show()
```

## 각 항목의 개수 표시

```py
# x에는 x축에 표시할 범주, data에는 원본 데이터 표시
chart = sns.countplot(x=column, data=df)
plt.show()
```
