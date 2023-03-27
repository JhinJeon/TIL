# Serializer 사용

- Django와 연결된 DB의 정보를 json 형식으로 전환할 때 사용한다.
- 반대로 json 파일을 DB에 저장하는 경우에는 Deserializer를 사용한다.
  - Deserializer를 사용할 때는 DB의 각 컬럼들로 정의해야 한다.

# ModelSerializer

- models.py에서 선언한 모델을 JSON 형식으로 전환할 때 사용한다.
- class Meta: 이하에 전환할 모델 이름과 필드(컬럼)를 입력하면 된다.
  - 모든 컬럼을 전환하려면 "\_\_all\_\_"을 입력한다/
