
# 모든 조합의 경우의 수를 구한다 => subset(부분집합), 시간 복잡도 : 0(2^n)
# 문제에서 N의 최대값이 최대 20 -> 2의 20승


def get_combinations_recur(arr, n):

    result = []
    if n == 1:  # 선택할 요소가 1인 경우, 각 요소 자체가 하나의 조합
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        # 현재 고정시켜 놓은 요소 다음부터 재귀로 넘김
        # 한개를 이미 골랐으니, 다음 재귀 넘길때는 한개를 빼서 넘김
        for rest in get_combinations_recur(arr[i+1:], n-1):
            result.append([elem] + rest)


    return result

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    def get_min_tower_height(N, B, heights):
        min_height = float('inf')   # 조합을 구현하고, 최소값을 찾으면 최소값으로 갱신

        # height(N) 명에 대해서 1명을 선택하는 것 부터 N명 모두 선택하는 것 까지
        # 모든 조합을 구하고 그 조합들의 합을 구하고 거기서 B를 넘는 것 중 가장 작은 것 구할거다
        for r in range(1, N+1):     # 1명부터 N명 선택하는 조합을 구하기 위해 순회
            for comb in get_combinations_recur(heights, r):     # heights 에서 r명 선택한 조합
                total_height = sum(comb)
                # 문제의 조건 : B보다 크거나 같으면 됨
                if total_height >= B:
                    min_height = min(min_height, total_height)
        
        return min_height

    res = get_min_tower_height(N, B, arr)

    print(f'#{tc} {res - B}')
