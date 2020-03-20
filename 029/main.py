# Conditions
# Only one time, one disucs can be moved
# a discus can not be seat on a smaller discus


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a,c,b)
        print("%d번 원반을 %c에서 %c로 옮김"%(n,a,b))
        hanoi(n-1,c,b,a)

if __name__ == "__main__":
    print("원반의 개수: ")
    n = int(input())
    hanoi(n,'a','b','c')
