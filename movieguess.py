from random import choice

movies = [
    "CASABLANCA",
    "GLADIATOR",
    "BRAVEHEART",
    "TITANIC",
    "AVATAR",
    "MEMENTO",
    "INCEPTION",
    "INTERSTELLAR",
    "FIGHT CLUB",
    "THE DARK KNIGHT",
    "PULP FICTION",
    "FORREST GUMP",
    "JURASSIC PARK",
    "THE MATRIX",
    "GOODFELLAS",
    "ALIEN",
    "THE DEPARTED",
    "BLACK HAWK DOWN",
    "GLADIATOR",
    "THE SHAWSHANK REDEMPTION"
]

def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range(n):
        if letters[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = "".join(str(x) for x in temp)
    return qn

def is_present(letter, movie):
    return letter in movie

def unlock(qn, movie, letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if ref[i] == ' ' or ref[i] == letter:
            temp.append(ref[i])
        else:
            if qn_list[i] == '*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new = "".join(str(x) for x in temp)
    return qn_new

def play():
    p1name = input("Player 1! Please enter your name: ")
    p2name = input("Player 2! Please enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True

    while willing:
        max_points = 10
        if turn % 2 == 0:
            # Player 1
            print(p1name, "Your turn")
            picked_movie = choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            points = max_points
            complimentary_guess = True
            
            while not_said:
                letter = input("Your letter: ")
                if complimentary_guess:
                    complimentary_guess = False
                else:
                    points -= 1

                if is_present(letter, picked_movie):
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    if points > 0:
                        d = int(input("Press 1 to guess the movie or 2 to unlock another letter: "))
                        if d == 1:
                            ans = input("Your answer: ")
                            if ans == picked_movie:
                                pp1 += points
                                print("Correct")
                                not_said = False
                                print(p1name, "Your score:", pp1)
                            else:
                                print("Wrong answer. Try again.")
                    else:
                        print("No more points left. The answer was:", picked_movie)
                        not_said = False
                else:
                    print(letter, "not found")
                    if points <= 0:
                        print("No more points left. The answer was:", picked_movie)
                        not_said = False
            
            c = int(input("Press 1 to continue or 0 to quit: "))
            if c == 0:
                print(p1name, "Your score:", pp1)
                print(p2name, "Your score:", pp2)
                print("Thanks for playing")
                print("Have a nice day!")
                willing = False

        else:
            # Player 2
            print(p2name, "Your turn")
            picked_movie = choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            points = max_points
            complimentary_guess = True
            
            while not_said:
                letter = input("Your letter: ")
                if complimentary_guess:
                    complimentary_guess = False
                else:
                    points -= 1

                if is_present(letter, picked_movie):
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    if points > 0:
                        d = int(input("Press 1 to guess the movie or 2 to unlock another letter: "))
                        if d == 1:
                            ans = input("Your answer: ")
                            if ans == picked_movie:
                                pp2 += points
                                print("Correct")
                                not_said = False
                                print(p2name, "Your score:", pp2)
                            else:
                                print("Wrong answer. Try again.")
                    else:
                        print("No more points left. The answer was:", picked_movie)
                        not_said = False
                else:
                    print(letter, "not found")
                    if points <= 0:
                        print("No more points left. The answer was:", picked_movie)
                        not_said = False
            
            c = int(input("Press 1 to continue or 0 to quit: "))
            if c == 0:
                print(p1name, "Your score:", pp1)
                print(p2name, "Your score:", pp2)
                print("Thanks for playing")
                print("Have a nice day!")
                willing = False

        turn += 1

play()