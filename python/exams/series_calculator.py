from math import floor

series_name = input()
seasons_number = int(input())
episode_number = int(input())
time_per_episode_noadds = float(input())

adds_time = time_per_episode_noadds * 0.20
episode_with_adds = adds_time + time_per_episode_noadds
additional_time = seasons_number * 10
total_time = episode_with_adds * episode_number * seasons_number + additional_time
print(f"Total time needed to watch the {series_name} series is {floor(total_time)} minutes.")