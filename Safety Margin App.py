# a=이음 효율
# b=적용 안전율
# mode=모드 계수
# number=하중 계수
# wight1=중량물 무게
# weight2=양중함 무게
# weight3=줄걸이 용구 무게

class Safety :
    def __init__(self,weight1,weight2,weight3, num_slings, sling_method):
        self.weight1 = weight1  #중량물 무게
        self.weight2 = weight2  #양중함 무게
        self.weight3 = weight3  #줄걸이 용구 무게
        self.num_slings = num_slings  #줄걸이 수
        self.sling_method = sling_method  #줄걸이 방법

    def chain(self):

        weight = self.weight1 + self.weight2 + self.weight3
        result1 = 0
        result2 = 0
        result3 = 0
        a = 100  # 이음 효율
        b = 5    # 적용 안전율

        sling_capacity = (weight * b * number)/(self.num_slings * mode*(a/100))
        shackle_capacity = sling_capacity
        result1 = result1+weight
        result2 = result2 + sling_capacity
        result3 = result3 + shackle_capacity
        if weight<5000:

            print('총 양중 무게:', weight,'톤','작업 가능','필요 줄걸이 용량(1줄당):',sling_capacity,'톤','필요 샤클 용량(1개당):',shackle_capacity,'톤')
        else:
            print('총 양중 무게:',weight,'톤','작업 불가능',weight-500,'톤','초과')
        return result1,result2,result3
    def nylon_sling(self):
        weight = self.weight1 + self.weight2 + self.weight3
        result1 = 0
        result2 = 0
        result3 = 0
        a = 100
        b = 1
        sling_capacity =  (weight * b * number) / (self.num_slings * mode * (a / 100))
        shackle_capacity = sling_capacity
        result1 = result1 + weight
        result2 = result2 + sling_capacity
        result3 = result3 + shackle_capacity
        if weight < 2000:
            print('총 양중 무게:',weight,'톤','작업 가능','필요 줄걸이 용량(1줄당):','톤',sling_capacity,'필요 샤클 용량(1개당):',shackle_capacity,'톤')
        else:
            print('총 양중 무게:',weight,'톤', '작업 불가능', weight-200,'톤', '초과')
        return result1, result2, result3
    def wire_rope(self):
        weight = self.weight1 + self.weight2 + self.weight3
        result1 = 0
        result2 = 0
        result3 = 0
        a = 80
        b = 5
        sling_capacity = (weight * b * number) / (self.num_slings * mode * (a / 100))
        shackle_capacity= sling_capacity/b
        result1 = result1 + weight
        result2 = result2 + sling_capacity
        result3 = result3 + shackle_capacity
        if weight < 3000:
            print('총 양중 무게:',weight,'톤','작업 가능','필요 줄걸이 용량(1줄당):','톤',sling_capacity,'필요 샤클 용량(1개당):',shackle_capacity,'톤')
        else:
            print('총 양중 무게:',weight,'톤', '작업 불가능', weight-300,'톤','초과')
        return result1, result2, result3

while True:
    type1 = input('줄걸이 종류를 입력 하세요:[chain,wire_rope,nylon_sling]:')
    weight1 = float(input('중량물 무게를 입력 하세요(단위:톤):'))
    weight2 = float(input('양중함 무게를 입력 하세요(단위:톤).[[0.1~1]:'))
    weight3 = float(input('줄걸이 용구 무게를 입력 하세요(단위:톤).:'))
    num = int(input('줄걸이 수를 입력 하세요.[1,2,3,4]:'))
    method = input('줄걸이 방법을 입력 하세요[1자 걸이, 초크 걸이, U자형 걸이]:')
    if num < 2:
        number = 1  # 하중 계수
    else:
        number = 1.155
    if method == '1자 걸이':
        mode = 1  # 모드 계수
    elif method == '초크 걸이':
        mode = 0.8
    elif method == 'U자형 걸이':
        mode = 2
    my_info=Safety(weight1,weight2,weight3,num,method,)

    if type1 == 'chain':
        my_info.chain()
    elif type1 == 'nylon_sling':
        my_info.nylon_sling()
    elif type1 == 'wire_rope':
        my_info.wire_rope()
    else:
        print('잘못된 값을 입력 하셨습니다.')

    answer = input("계속 해서 다른 값으로 계산 하시겠습니까? (y/n): ")
    if answer.lower() != 'y':
        print("프로그램을 종료합니다.")
        break



