# 문제 1

# 문제 2
# 주어진 리스트 중 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수
def f4(given_list):
    even_list = list(filter(lambda x: x % 2 == 0, given_list))
    index_list = list(map(lambda x: given_list.index(x), even_list))
    return(sum(index_list))

# for test
test = [4,6,2,3,1,10]
print(f4(test))

# 문제 3
