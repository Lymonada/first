def divide_people_into_teams(num_people, team_size):
    teams = []
    people = []

    # 사람 이름 한 번에 입력받기
    names = input(f"전체 인원의 이름을 공백으로 구분하여 입력하세요: ").split()

    if len(names) != num_people:
        print(f"입력한 이름 수({len(names)})가 총 인원 수({num_people})와 다릅니다.")
        return []

    people = names

    # 팀 나누기
    for i in range(0, num_people, team_size):
        team = people[i:i+team_size]
        teams.append(team)

    return teams

# 총 인원 수와 팀 크기 입력받기
num_people = int(input("총 인원 수를 입력하세요 (1~500 사이): "))
while num_people < 1 or num_people > 500:
    num_people = int(input("잘못된 입력입니다. 1~500 사이의 숫자를 입력하세요: "))

team_size = int(input("팀 크기를 입력하세요: "))
while team_size < 1 or team_size > num_people:
    team_size = int(input(f"잘못된 팀 크기입니다. 1~{num_people} 사이의 숫자를 입력하세요: "))

# 팀 출력하기
teams = divide_people_into_teams(num_people, team_size)
if not teams:
    print("입력한 이름 수가 잘못되어 팀 나누기를 할 수 없습니다.")
else:
    for i, team in enumerate(teams):
        print(f"{i+1}번 팀: {', '.join(team)}")

#'구분자'.join(리스트) -> 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.