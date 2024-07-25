import pandas as pd


class Safety:
    def __init__(self, weight1, weight2, weight3, num_slings, sling_method):
        self.weight1 = weight1  # 중량물 무게
        self.weight2 = weight2  # 양중함 무게
        self.weight3 = weight3  # 줄걸이 용구 무게
        self.num_slings = num_slings  # 줄걸이 수
        self.sling_method = sling_method  # 줄걸이 방법

    def chain(self):
        weight = self.weight1 + self.weight2 + self.weight3
        result1 = 0
        result2 = 0
        result3 = 0
        result4 = ''
        a = 100  # 이음 효율
        b = 5  # 적용 안전율

        sling_capacity = (weight * b * number) / (self.num_slings * mode * (a / 100))
        shackle_capacity = sling_capacity
        result1 = result1 + weight
        result2 = result2 + sling_capacity
        result3 = result3 + shackle_capacity

        if weight < 500:
            result4 = '작업 가능'
        else:
            result4 = '작업 불가능'

        return result1, result2, result3, result4

    def nylon_sling(self):
        weight = self.weight1 + self.weight2 + self.weight3
        result1 = 0
        result2 = 0
        result3 = 0
        result4 = ''
        a = 100
        b = 1

        sling_capacity = (weight * b * number) / (self.num_slings * mode * (a / 100))
        shackle_capacity = sling_capacity
        result1 = result1 + weight
        result2 = result2 + sling_capacity
        result3 = result3 + shackle_capacity

        if weight < 200:
            result4 = '작업 가능'
        else:
            result4 = '작업 불가능'

        return result1, result2, result3, result4

    def wire_rope(self):
        weight = self.weight1 + self.weight2 + self.weight3
        result1 = 0
        result2 = 0
        result3 = 0
        result4 = ''
        a = 80
        b = 5

        sling_capacity = (weight * b * number) / (self.num_slings * mode * (a / 100))
        shackle_capacity = sling_capacity / b
        result1 = result1 + weight
        result2 = result2 + sling_capacity
        result3 = result3 + shackle_capacity

        if weight < 300:
            result4 = '작업 가능'
        else:
            result4 = '작업 불가능'

        return result1, result2, result3, result4


# Prompt user inputs in a loop
result = []
while True:
    try:
        type1 = input('줄걸이 종류를 입력하세요: [1.chain, 2.nylon_sling, 3.wire_rope]: ')
        weight1 = float(input('중량물 무게를 입력하세요 (단위: 톤): '))
        weight2 = float(input('양중함 무게를 입력하세요 (단위: 톤): '))
        weight3 = float(input('줄걸이 용구 무게를 입력하세요 (단위: 톤): '))
        num = int(input('줄걸이 수를 입력하세요 [1, 2, 3, 4 중 선택]: '))
        method = input('줄걸이 방법을 입력하세요 [1. 1자 걸이, 2. 초크 걸이, 3. U자형 걸이]: ')

        if type1 not in ['1', '2', '3']:
            raise ValueError('잘못된 줄걸이 종류 입력.')
        if num not in [1, 2, 3, 4]:
            raise ValueError('잘못된 줄걸이 수 입력.')
        if method not in ['1', '2', '3']:
            raise ValueError('잘못된 줄걸이 방법 입력.')

    except ValueError as ve:
        print(f'입력 오류: {ve}')
        continue

    if num < 2:
        number = 1  # 하중 계수
    else:
        number = 1.155

    if method == '1':
        mode = 1  # 모드 계수
    elif method == '2':
        mode = 0.8
    elif method == '3':
        mode = 2

    my_info = Safety(weight1, weight2, weight3, num, method)

    if type1 == '1':
        result1, result2, result3, result4 = my_info.chain()
    elif type1 == '2':
        result1, result2, result3, result4 = my_info.nylon_sling()
    elif type1 == '3':
        result1, result2, result3, result4 = my_info.wire_rope()
    else:
        print('잘못된 값을 입력하셨습니다.')
        continue

    # Create a DataFrame with the results
    data = {
        '줄걸이 종류': type1,
        '줄걸이 수': num,
        '줄걸이 방법': method,
        '중량물 무게 (톤)': result1,
        '필요 줄걸이 용량 (톤)': round(result2,2),
        '필요 샤클 용량 (톤)': round(result3,2),
        '작업 가능 여부': result4
    }
    result.append(data)
    df = pd.DataFrame(result)

    # Export to Excel
    excel_filename = 'output.xlsx'
    df.to_excel(excel_filename, index=False)
    print(f"결과가 {excel_filename} 파일로 저장되었습니다.")

    answer = input("계속해서 다른 값으로 계산하시겠습니까? (yes/no): ")
    if answer.lower() != 'yes':
        print("프로그램을 종료합니다.")
        break
