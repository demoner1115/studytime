import json

with open('studytie.json', 'r', encoding="utf-8") as f:
    study = json.load(f)

time_list = [record["시간"] for record in study]
total_time = sum(record["시간"] for record in study)
p = len(time_list)

answer = total_time // p
print("총 평균 공부 시간은 {}분 입니다.".format(answer))
