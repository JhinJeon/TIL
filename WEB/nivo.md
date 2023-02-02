# nivo

- React에서 사용 가능한 그래프 디자인 라이브러리
- 차트, 원형 그래프 등 데이터 요약본을 보여줄 때 용이하다.

# 환경 설정

```
npm install @nivo/core

yarn add @nivo/core
```

# 원형 차트

- 원형 차트를 사용하려면 @nivo/pie를 추가로 설치해야 한다.

```
npm install @nivo/pie

yarn add @nivo/pie
```

## 도넛 차트 중앙에 레이블 넣기

1. layers=에 커스텀 레이어 넣기

```js
<ResponsivePie
    {/* ...중략 */}
    {/* 앞의 4개 변수는 기본 값 */}
    layers={["arcs", "arcLabels", "arcLinkLabels", "legends", CenteredMetric]}
    {/* ...중략 */}
/>
```

2. 커스텀 레이어 값 설정

```js
const CenteredMetric = ({ dataWithArc, centerX, centerY }) => {
  let total = 0;
  dataWithArc.forEach((datum) => {
    total += datum.value;
  });

  const win = recentRecord[0].value;
  const lose = recentRecord[1].value;

  return (
    <>
      {/* text 태그를 여러 줄 집어넣으면 여러 줄에 걸쳐서 나온다. */}
      {/* 텍스트 색상을 바꾸려면 fill=에 색상 코드 입력 */}
      <text
        x={centerX}
        y={centerY - 10}
        textAnchor="middle"
        dominantBaseline="central"
        fill="white"
      >
        최근 {total} 전
      </text>
      <text
        x={centerX}
        y={centerY + 10}
        textAnchor="middle"
        dominantBaseline="central"
        fill="white"
      >
        {win}승 {lose}패
      </text>
    </>
  );
};
```
