


def main():
    
    ctemps = [6, 11, 13, 16, 11, 23, 45, 33, 13, 24, 12, 17, 22]

    far_temps1 = [(t * 9/5) + 32 for t in ctemps]
    far_temps2 = {(t * 9/5) + 32 for t in ctemps}

    print(far_temps1)
    print(far_temps2)


    temp_str = "The quick brown fox jumped over the lazy dog"
    characters = {c.upper() for c in temp_str if not c.isspace() }
    print(characters)

if __name__ == "__main__":
    main()
