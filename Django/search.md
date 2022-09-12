# 게시글 검색 기능 구현

django의 filter() 이용

```python
filtered = Movie.objects.filter(필터 조건)
```

# 게시글 내 필터(숫자값을 기준으로 필터링할 때)

- '변수명__연산자' = 값 으로 표시
- 연산자는 gt, gte, lt, lte(순서대로 >, >=, <, <=)

```python
def foryou(request):
    movies = Movie.objects.all().filter(score__gte = 4)
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)
```