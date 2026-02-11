import json

subject = input("과목: ")
time = int(input("시간(분단위 숫자만 입력해주세요): "))
memo = input("메모: ")

with open('studytie.json', 'r', encoding="utf-8") as f:
    study = json.load(f)

record = {
    "과목": subject,
    "시간": time,
    "메모": memo,
}

study.append(record)

with open('studytie.json', 'w', encoding='utf-8') as f:
    json.dump(study, f, ensure_ascii=False)

print("공부기록 저장 완료")
