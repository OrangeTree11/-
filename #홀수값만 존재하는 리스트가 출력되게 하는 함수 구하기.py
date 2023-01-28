#홀수값만 존재하는 리스트가 출력되게 하는 함수 구하기
num_list = [1 ,5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list) :
        answer = [num_list[x] for x in range(len(num_list)) if num_list[x] % 2 == 1] #list comprehension은 굉장히 파이토닉한 코드작성법. 잘 알아놓아야 한다.

        return answer


print(get_odd_num(num_list))