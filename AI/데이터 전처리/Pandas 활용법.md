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

## 파라미터 간 유사도를 구할 때?

- 원본 행렬과 원본 행렬을 전치(transpose)한 행렬을 곱한 값을 유사도로 정한다.
- transpose를 하려면 데이터프레임.transpose()로 전환할 수 있다.
  - 또는 데이터프레임.T 를 사용할 수도 있다.

```py
tp_df = df.transpose()
tp_df = df.T
```

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

## 특정 행(구분) 지우기

- df.drop(labels=[지울 행], axis=(0: 가로, 1:세로), inplace=(True/False))
- inplace=True시 원본 데이터를 변경하고, inplace=False 시 새로운 데이터프레임 객체를 생성한다.

```py
df.drop(labels=["AREA_NM"], axis=1, inplace=True)
```

## 결측치가 들어있는 행/열 제거

- df.dropna(subset=["지울 행"], how=(all/any), inplace=(True/False))
- how=any 시 subset에 있는 행 중 하나 이상이 결측치가 있을 때 제거하고, all 시 subset의 모든 행이 결측치가 있을 때 제거
- subset을 설정하지 않으면 df의 모든 행을 대상으로 시행

```py
df.dropna(subset=["AGE_FLAG_NM", "SEXDSTN_FLAG_NM"], how='any', inplace=True)
```
