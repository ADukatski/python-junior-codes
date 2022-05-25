time_for_pic = int(input())
number_scenes = int(input())
time_for_scene = int(input())

prepare = time_for_pic * 0.15
scene_time = number_scenes * time_for_scene
need = prepare + scene_time

if need > time_for_pic:
    diff = abs(need - time_for_pic)
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")
else:
    diff = abs(need - time_for_pic)
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")