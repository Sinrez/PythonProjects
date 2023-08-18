


def main():
    
    ctemps = [0, 10, 44, 100, 120]

    temp_dict = {t: (t * 9/5) + 32 for t in ctemps if t < 100}
    print(temp_dict)
    print(temp_dict[10])


    
    team1 = {"Adams": 14, "Pearse": 28, "Hendrics": 44, "Ericcson": 1}
    team2 = {"Parquette": 16, "Duvall": 67, "Lafleur": 5}

    new_team = {k: v for team in (team1, team2) for k, v in team.items()}
    print(new_team)



if __name__ == "__main__":
    main()