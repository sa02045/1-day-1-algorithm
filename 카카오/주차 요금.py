# 코드
import math

def solution(fees, records):
    cars_park_time = {}
    answer = []
    
    for i in range(len(records)):
        [in_time, in_car_number, in_info] = records[i].split(" ")
        if in_info == "IN":
            out_time = get_out_time(in_car_number,i,records)
            park_time = get_park_time(in_time,out_time) 
            if in_car_number in cars_park_time:
                cars_park_time[in_car_number] += park_time
            else :
                cars_park_time[in_car_number] = park_time
    
    # 자동차 번호판 오름차순으로 정렬한다
    cars_park_time = sorted(cars_park_time.items())

	# 주차요금을 계산하고 답에 추가한다.
    for (car_number,park_time) in cars_park_time:
        answer.append(get_fee(fees,park_time))
    return answer
                    


# 출차 시각을 찾는다. 만약 없으면 "23:59"에 나간것으로 간주한다
def get_out_time(in_car_number,idx,records):
    for j in range(idx,len(records)):
        [out_time, out_car_number, out_info] = records[j].split(" ")
        if in_car_number == out_car_number and out_info == "OUT":
            return out_time
    return "23:59"

# 주차 시간을 계산한다. 전부 "분"으로 변환후 계산했다.
def get_park_time(in_time,out_time):
    return  (int(out_time[:2]) * 60 + int(out_time[3:])) - (int(in_time[:2]) * 60 + int(in_time[3:]))
        
# 주차 요금을 계산한다
def get_fee(fees,park_time):
    [base_time,base_fee,per_time,per_fee] = fees
    if park_time <= base_time:
        return base_fee
    else:
        return base_fee + math.ceil((park_time-base_time) / per_time) * per_fee