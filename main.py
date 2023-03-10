# 예제 4-1 상하좌우 문제

# 공간의 크기를 나타내는 N 입력받기
n = int(input())
x, y = 1, 1  #현재 위치

# 이동계획 세우기
# L,R,U,D로 받기
plans = input.split()

# L,R,U,D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하자
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행하기
  x, y = nx, ny

print(x, y)
