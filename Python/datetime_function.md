## Datetime

- 오늘 날짜를 불러올 때 datetime 라이브러리 활용
    ```python
    import datetime
    today = datetime.datetime.now()
    ```
- 연/월/일 값을 사용할 때는 today:%y, today:%m, today:%d 활용
    ```python
    import datetime
    today = datetime.datetime.now()
    print(f'오늘은 {today:%y}-{today:%m}-{today:%d}')