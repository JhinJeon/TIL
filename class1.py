class Factory:

    type_classification = ['A', 'B', 'C', 'D']
    # type_classification 설명
    # A : 승용차
    # B : 승합차
    # C : 트럭
    # D : 버스
    type_name = ['승용차', '승합차', '트럭', '버스']
    segment_list = ['A', 'B', 'C', 'D', 'E', 'F']

    # 초기 정보 입력
    # type : 차종(type_classification) : A, B, C, D 중 하나 입력
    # segment : 차급(세그먼트) : A, B, C, D ,E, F 중 하나 입력

    def __init__(self, type, segment):
        self.type = type
        self.segment = segment

    # 코드네임 : 차종(type) + 차급(segment)으로 구성
    def codename(self):
        return f'{self.type}{self.segment}'

    # type_classification에 입력된 값을 바탕으로 차종을 한글로 표시
    def print_type_name(self):
        # type 값이 들어있는 인덱스 번호를 반환받아 type_name에서 알맞은 값 찾기
        return self.type_name[self.type_classification.index(self.type)]

    # build_date = 연도 4자리 + 주(Week) 2자리 + 일(Day) 1자리로 구성된 7자리의 수
    # 일 기준 : 1부터 5까지 월~금에 대입
    # 예) 2022152 : 2022년 15번째 주의 화요일(4월 5일)에 생산됨

    # 시리얼 넘버 생성 : 차종 + 생산일자(년도의 경우 뒤 2자리만) + 히든 코드(이하 설명)
    def create_serial_number(self, build_date):
        self.build_date = build_date
        return f'{self.type}{str(build_date)[2:]}{self.create_hidden_code()}'

    # 히든 코드(시리얼 넘버의 맨 마지막에 들어가는 고유 값) 생성
    @staticmethod
    def create_hidden_code():
        import random
        # hidden_code = 16진수의 고유 값 중에서 하나를 랜덤으로 선택
        hidden_code = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E']
        return random.choice(hidden_code)


Hwasung = Factory('A', 'C')
Gwangju = Factory('D', 'F')
Ulsan = Factory('B', 'A')
print(Hwasung.codename())
print(Gwangju.print_type_name())
print(Ulsan.create_serial_number(2022223))
