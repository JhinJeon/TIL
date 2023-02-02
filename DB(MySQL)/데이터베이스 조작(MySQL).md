# 데이터베이스 생성

```sql
CREATE DATABASE dbname;
```

# 테이블 생성

```sql
CREATE TABLE tablename
(
    _id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(20) NOT NULL,
    price INT NOT NULL,
    is_sold BOOLEAN NOT NULL default 0
) ENGINE=INNODB;
```

# 데이터 삽입

```sql
INSERT INTO tablename
(product_name, price, is_sold)
VALUE('두부', 2000, 0);
```

# 데이터 조회

1. 테이블 전체를 조회할 때

```sql
DESCRIBE tablename;
```

2. 테이블에서 특정 기준으로 데이터를 필터링할 때

```sql
SELECT * FROM tablename;
```

# 외래 키 정의

- ADD CONSTRAINT를 추가하는 이유는 테이블에 '외래 키'라는 제약조건을 추가하는 코드이기 때문

```sql
ALTER TABLE tablename
    ADD CONSTRAINT changekey
    FOREIGNKEY(id)
    REFERENCES tablename2(id)
    ON UPDATE CASCADE ON DELETE CASCADE;
```