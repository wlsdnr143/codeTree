# 재귀함수를 이용한 n자리수의 가능한 모든 2진수 출력 프로그램

n = int(input())  # n 자리수
answer = []  # 2진수가 저장될 리스트


def print_answer():  # 리스트에 저장된 2진수 출력 함수
    for digit in answer:
        print(digit, end="")
    print()


def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return

    answer.append(0)
    choose(curr_num + 1)
    answer.pop()

    answer.append(1)
    choose(curr_num + 1)
    answer.pop()

    return


# 여기서 return 을 하게되면 함수가 끝나는 것이 아니라 호출하기 전 함수로 돌아감
# 0 0 0 을 한 후 choose(4)를 불렀을때 조건이 맞아 출력 한 후 return 을 하게되면 0 0 0으로 돌아간 후
# answer.pop 하고 1을 삽입 -> 0 0 1 이 만들어짐

choose(1)  # 첫번째 자리부터 시작
