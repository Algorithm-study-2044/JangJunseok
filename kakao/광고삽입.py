# 3:35시작. 1차시도 실패. 12/15 테스트케이스 통과.

# 가장 빠른 log와 가장 느린 log를 경계로 두고,
# 1초씩 더하면서, 몇명이 겹치는지. 
# 그러면 대충 초단위로 이런 array가 나올듯.

# 시작이 3600초 -> 끝이 4200초다.
# 그러면 600짜리 배열을 만든다.

# [1,2,3,3,3,3,3,3,4,2,1,1,]
# 이렇게 만든다음에, 일정길이의 구간합을 가장 크게 만들면 되는거임.
# 예를 들어 1초짜리다? 그러면 1 길이의 구간합.

def time_to_seconds(time_string):
    res = 0
    arr = time_string.split(":")
    res += int(arr[0]) * 3600
    res += int(arr[1]) * 60
    res += int(arr[2])
    return res

def seconds_to_time(seconds):
    time = seconds // 3600
    minute = seconds % 3600 // 60
    second = seconds % 60
    return f"{str(time).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"

def solution(play_time, adv_time, logs):
    secs = []
    for lg in logs:
        s1, s2 = lg.split("-")
        e1, e2 = time_to_seconds(s1), time_to_seconds(s2)
        secs.append((e1,e2))
        
    stream = [0] * (time_to_seconds(play_time))
        
    for st,ed in secs:
        for seconds in range(st,ed):
            stream[seconds] += 1
    
    adv_length = time_to_seconds(adv_time)
    value = sum(stream[:adv_length])
    max_value = value
    
    start_idx = 0
    max_times = [start_idx]
    
    while start_idx < len(stream)-adv_length:
        value -= stream[start_idx]
        value += stream[start_idx + adv_length]
        if value >= max_value:
            if value > max_value:
                max_times = []
            max_value = value
            # 이 부분이 헷갈렸다. 그러니까 지금 시간을 증가시킨 상황이니까, 
            # 증가된 시간을 넣었어야 했는데.
            max_times.append(start_idx+1)
        start_idx += 1
    
    answer = seconds_to_time(max_times[0])

    return answer



# 2차시도.

def time_to_seconds(time_string):
    res = 0
    arr = time_string.split(":")
    res += int(arr[0]) * 3600
    res += int(arr[1]) * 60
    res += int(arr[2])
    return res

def seconds_to_time(seconds):
    time = seconds // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60
    return f"{str(time).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"

def solution(play_time, adv_time, logs):
    play_seconds = time_to_seconds(play_time)
    adv_seconds = time_to_seconds(adv_time)
    
    # 시청자 수를 기록할 배열 (0부터 play_seconds까지)
    viewers = [0] * (play_seconds + 1)
    
    # 로그를 통해 각 시간대별 시청자 수를 기록
    for lg in logs:
        start, end = lg.split("-")
        start_sec = time_to_seconds(start)
        end_sec = time_to_seconds(end)
        viewers[start_sec] += 1
        if end_sec < play_seconds:
            viewers[end_sec] -= 1
    
    # 누적합 계산 (Prefix Sum)
    for i in range(1, len(viewers)):
        viewers[i] += viewers[i - 1]
    
    # 슬라이딩 윈도우를 사용하여 최대 시청 시간 계산
    max_viewers = sum(viewers[:adv_seconds])
    current_viewers = max_viewers
    start_time = 0
    
    for i in range(1, play_seconds - adv_seconds + 1):
        current_viewers = current_viewers - viewers[i - 1] + viewers[i + adv_seconds - 1]
        if current_viewers > max_viewers:
            max_viewers = current_viewers
            start_time = i
    
    answer = seconds_to_time(start_time)
    return answer
