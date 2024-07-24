class Safety:
    def __init__(self, weight1, weight2, weight3, num_slings, sling_method):
        self.weight1 = weight1  # 중량물 무게
        self.weight2 = weight2  # 양중함 무게
        self.weight3 = weight3  # 줄걸이 용구 무게
        self.num_slings = num_slings  # 줄걸이 수
        self.sling_method = sling_method  # 줄걸이 방법

    def calculate_capacity(self):
        weight_total = self.weight1 + self.weight2 + self.weight3

        if self.sling_method == '1':
            a = 100  # 이음 효율
            b = 5  # 적용 안전율
            if weight_total < 500:
                sling_capacity = (weight_total * b) / (self.num_slings * (a / 100))
                shackle_capacity = sling_capacity
                result = '작업 가능'
            else:
                result = '작업 불가능'
        elif self.sling_method == '2':
            a = 100
            b = 1
            if weight_total < 200:
                sling_capacity = (weight_total * b) / (self.num_slings * (a / 100))
                shackle_capacity = sling_capacity
                result = '작업 가능'
            else:
                result = '작업 불가능'
        elif self.sling_method == '3':
            a = 80
            b = 5
            if weight_total < 300:
                sling_capacity = (weight_total * b) / (self.num_slings * (a / 100))
                shackle_capacity = sling_capacity / b
                result = '작업 가능'
            else:
                result = '작업 불가능'
        else:
            raise ValueError('잘못된 줄걸이 방법 입력')

        print(f'총 양중 무게: {weight_total} 톤')
        print(f'필요 줄걸이 용량(1줄당): {round(sling_capacity, 2)} 톤')
        print(f'필요 샤클 용량(1개당): {round(shackle_capacity, 2)} 톤')
        print(result)


while True:
    try:
        type1 = input('줄걸이 종류를 입력하세요 (1: 체인 2: 나일론 슬링, 3: 와이어 로프): ')
        weight1 = float(input('중량물 무게를 입력하세요 (단위: 톤): '))
        weight2 = float(input('양중함 무게를 입력하세요 (단위: 톤): '))
        weight3 = float(input('줄걸이 용구 무게를 입력하세요 (단위: 톤): '))
        num = int(input('줄걸이 수를 입력하세요 (1, 2, 3, 4 중 선택): '))
        method = input('줄걸이 방법을 입력하세요 (1: 1자 걸이, 2: 초크 걸이, 3: U자형 걸이): ')

        if type1 not in ['1', '2', '3']:
            raise ValueError('잘못된 줄걸이 종류 입력')
        if num not in [1, 2, 3, 4]:
            raise ValueError('잘못된 줄걸이 수 입력')
        if method not in ['1', '2', '3']:
            raise ValueError('잘못된 줄걸이 방법 입력')

    except ValueError as ve:
        print(f'입력 오류: {ve}')
        continue

    my_info = Safety(weight1, weight2, weight3, num, method)

    try:
        my_info.calculate_capacity()
    except ValueError as ve:
        print(f'오류 발생: {ve}')

    answer = input("계속해서 다른 값으로 계산하시겠습니까? (yes/no): ")
    if answer.lower() != 'yes':
        print("프로그램을 종료합니다.")
        break
