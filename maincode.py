#BRAVE NEW WORLD CHOOSE YOUR OWN ADVENTURE PROJECT
#Brave New World - Published in 1932 by Aldous Huxley
#Project by Mia Melishchuk
#English 4 Honors 2nd Period
#Ms. Conklin

def game():
    print("Brave New World, by Aldous Huxley, takes place in the year A.F. 632 in the World State. Eugenics and sleep conditioning are the World State’s means of adhering to their motto: “Community, Identity, Stability” (Huxley 1). In exchange for these things, the people have forsaken love and individuality, and instead focus on self-serving pleasures like having sex without dating exclusively and taking soma, a pleasure-inducing drug with a high that gives the consumer “a holiday from the facts.” One day, two people from the World State, Bernard Marx and Lenina Crowne, discover you, the player. You have grown up outside the World State's civilization, and Bernard, a member of the highest caste in the World State, takes a great interest in you. He offers to take you and your mother, who grew up in the World State, to London and allow you to experience \"civilized life\" for the first time. ")
    
    def playagain():
        print("\n\nYour game has ended. Thanks for playing! ", end="")
        choice = input("Do you want to play again?\n1: Yes\n2: No\n\n")
        if choice == "1":
            game()
        elif choice == "2":
            quit()
    path = "1.0 2.0 3.0 4.0"

    def row1():
        choice = input("\n\nDo you go with Bernard?\n1: Yes\n2: No\n\n")
        return choice
    path = path.replace("1.0", str("1." + row1()))

    def row2(row1path):
        if row1path == "1":
            print("\n\nYou have chosen to go with Bernard.")
            print("\nBernard has been showing you off like a trophy to everyone in London. His reputation has blossomed and he went from being disrespected by others to being regarded as highly important. One night, he asks you if you want to go to a very important event so he can show you off to the Arch-Community-Songster of Canterbury.")
            choice = input("Do you want to attend the event to help bolster Bernard's reputation?\n1: Yes\n2: No\n\n") 
            return choice
        if row1path == "2":
            print("\n\nYou have chosen to remain in your isolated community and not learn about the \"perfect civilization.\"")
            playagain()
    path = path.replace("2.0", str("2." + row2(path[2])))

    def row3(row1path, row2path):
        if row2path == "1":
            print("\n\nYou have chosen to help Bernard feed his need to be important. ")
            choice = input("Lenina admits that she has loved you since she met you, and she takes off her clothes and really wants to have sex with you. Do you want to indulge and have emotionless sex with her instead of developing this relationship?\n1: Yes\n2: No\n\n")
            return choice
        elif row2path == "2":
            print("\n\nYou have refused to be Bernard's show monkey or trophy and you would rather stay at home and read your Shakespeare book.")
            choice = input("Lenina admits that she has loved you since she met you, and she takes off her clothes and really wants to have sex with you. Do you want to indulge and have emotionless sex with her instead of developing this relationship?\n1: Yes\n2: No\n\n")
            return choice

    path = path.replace("3.0", str("3." + row3(path[2], path[6])))

    def row4(row1path, row2path, row3path):
        if row3path == "1":
            print("\n\nYou indulge Lenina (and yourself a little) and have passionate sex without connecting on an emotional level. You have pretty much disregarded the idea that human relationships are supposed to mean something and that sex should be a product of that.")
            choice = input("You think you can free the Deltas, one of the lowest castes of society, from their miserable lives by destroying their soma and forcing them to live as themselves. Do you do it?\n1: Yes\n2: No\n\n")
            return choice
        elif row3path == "2":
            print("\n\nYou refuse to have sex with Lenina. The idea that she's willing to throw herself at you is appalling, and you have to use physical force to push her away (you also may or may not slap her and threaten to kill her, but we don't talk about page 199). Let's be real here, John is far from okay.")
            choice = input("You think you can free the Deltas, one of the lowest castes of society, from their miserable lives by destroying their soma and forcing them to live as themselves. Do you do it?\n1: Yes\n2: No\n\n")
            return choice

    path = path.replace("4.0", str("4." + row4(path[2], path[6], path[10])))

    def row6(row1path, row2path, row3path, row4path):
        if row2path == "1":
            if row3path == "1":
                if row4path == "1":
                    print("\n\nYou started throwing the Deltas' soma out of a window and they attacked you. Your friend Helmholtz joined you in fighting them off while Bernard tried to sneak away, and the police came and arrested you all. You were taken to the World Controller's office, where you and he talk about philosophy, science, and religion. Although you've done okay at aligning yourself with normal behavior within the World State, you still cannot accept the fact that people can be happy while knowing they are in a lower place than someone else. Your abnormal ideas of equality and freedom can cause disorder in this perfectly conditioned society, so you must be sent into exile. The World Controller takes a little bit of a liking to you, however, and allows you to choose which island you will go to.")
                    choice = input("\n\nPick an island: \n1: Iceland - it is very cold and remote, but the people there think the most like you and the World Controller views it as a reward.\n2: Samoa - the climate is very warm and tropical (according to the World Controller) and you will probably have an easier life than at any of the other island options.\n3: The Falkland Islands - the climate is very harsh, with heavy winds and storms. You will probably be very unhappy there, but your hardships will inspire you to think and write more. Bernard and Helmholtz will be there as well. ")
                    if choice == "1":
                        print("\nYou will be sent to Iceland.\n")
                        playagain()
                    elif choice == "2":
                        print("\nYou will be sent to Samoa.\n")
                        playagain()
                    elif choice == "3":
                        print("\nYou will be sent to the Falkland Islands.\n")
                        playagain()
                    
                elif row4path == "2":
                    print("\n\nYou have chosen to accept the way the world works. The Deltas are happier if they take soma and don't think about how they have been engineered to not feel real feelings and to enjoy having a horrible job and being stupid and looked down upon by everyone else. You won't get in the way of that. However, due to your upbringing and the rebellious natures of your friends Bernard and Helmholtz, you are taken to the World Controller's office for a talk. You have done a wonderful job of adapting to the World State's conditioning and behaviors, but you still pose a risk to society should your ideas of Shakespeare and freedom come to light. ")
                    choice = input("You are supposed to go into exile on an island of your choice to be under the World Controller's observation, but you have the ability to run away and live in isolation outside of the civilization. Do you escape?\n1: Yes\n2: No\n\n")
                    if choice == "1":
                        print("\n\nYou escape and go live in an abandoned lighthouse away from people. You are soon discovered, however, and after people pester you and treat you like a zoo animal and you brutally attack Lenina and take soma, you are so distraught with your actions and plagued by your everlasting guilt that you kill yourself.\n")
                        playagain()
                    elif choice == "2":
                        choice = input("\n\nPick an island: \n1: Iceland - it is very cold and remote, but the people there think the most like you and the World Controller views it as a reward.\n2: Samoa - the climate is very warm and tropical (according to the World Controller) and you will probably have an easier life than at any of the other island options.\n3: The Falkland Islands - the climate is very harsh, with heavy winds and storms. You will probably be very unhappy there, but your hardships will inspire you to think and write more. Bernard and Helmholtz will be there as well. ")
                        if choice == "1":
                            print("\nYou will be sent to Iceland.\n")
                            playagain()
                        elif choice == "2":
                            print("\nYou will be sent to Samoa.\n")
                            playagain()
                        elif choice == "3":
                            print("\nYou will be sent to the Falkland Islands.\n")
                            playagain()

            elif row3path == "2":
                if row4path == "1":
                    print("\n\nYou started throwing the Deltas' soma out of a window and they attacked you. Your friend Helmholtz joined you in fighting them off while Bernard tried to sneak away, and the police came and arrested you all. You were taken to the World Controller's office, where you and he talk about philosophy, science, and religion. You haven't done a great job of aligning yourself with normal behavior within the World State, as you still cannot accept the benefits of self-serving pleasure or the fact that people can be happy while knowing they are in a lower place than someone else. Your abnormal ideas of equality, relationships, and freedom can cause disorder in this perfectly conditioned society, so you must be sent into exile. ")
                    choice = input("You are supposed to go into exile on an island of your choice to be under the World Controller's observation, but you have the ability to run away and live in isolation outside of the civilization. Do you escape?\n1: Yes\n2: No\n\n")
                    if choice == "1":
                        print("\n\nYou escape and go live in an abandoned lighthouse away from people. You are soon discovered, however, and after people pester you and treat you like a zoo animal and you brutally attack Lenina and take soma, you are so distraught with your actions and plagued by your everlasting guilt that you kill yourself.\n")
                        playagain()
                    elif choice == "2":
                        choice = input("\n\nPick an island: \n1: Iceland - it is very cold and remote, but the people there think the most like you and the World Controller views it as a reward.\n2: Samoa - the climate is very warm and tropical (according to the World Controller) and you will probably have an easier life than at any of the other island options.\n3: The Falkland Islands - the climate is very harsh, with heavy winds and storms. You will probably be very unhappy there, but your hardships will inspire you to think and write more. Bernard and Helmholtz will be there as well. ")
                        if choice == "1":
                            print("\nYou will be sent to Iceland.\n")
                            playagain()
                        elif choice == "2":
                            print("\nYou will be sent to Samoa.\n")
                            playagain()
                        elif choice == "3":
                            print("\nYou will be sent to the Falkland Islands.\n")
                            playagain()
                    
                elif row4path == "2":
                    print("\n\nYou have chosen to accept the way the world works. The Deltas are happier if they take soma and don't think about how they have been engineered to not feel real feelings and to enjoy having a horrible job and being stupid and looked down upon by everyone else. You won't get in the way of that. However, due to your upbringing and the rebellious natures of your friends Bernard and Helmholtz, you are taken to the World Controller's office for a talk. You have done an okay job of adapting to the World State's conditioning and behaviors, but you still pose a risk to society should your ideas of Shakespeare and freedom come to light. ")
                    choice = input("You are supposed to go into exile on an island of your choice to be under the World Controller's observation, but you have the ability to run away and live in isolation outside of the civilization. Do you escape?\n1: Yes\n2: No\n\n")
                    if choice == "1":
                        print("\n\nYou escape and go live in an abandoned lighthouse away from people. You are soon discovered, however, and after people pester you and treat you like a zoo animal and you brutally attack Lenina and take soma, you are so distraught with your actions and plagued by your everlasting guilt that you kill yourself.\n")
                        playagain()
                    elif choice == "2":
                        choice = input("\n\nPick an island: \n1: Iceland - it is very cold and remote, but the people there think the most like you and the World Controller views it as a reward.\n2: Samoa - the climate is very warm and tropical (according to the World Controller) and you will probably have an easier life than at any of the other island options.\n3: The Falkland Islands - the climate is very harsh, with heavy winds and storms. You will probably be very unhappy there, but your hardships will inspire you to think and write more. Bernard and Helmholtz will also be there. ")
                        if choice == "1":
                            print("\nYou will be sent to Iceland.\n")
                            playagain()
                        elif choice == "2":
                            print("\nYou will be sent to Samoa.\n")
                            playagain()
                        elif choice == "3":
                            print("\nYou will be sent to the Falkland Islands.\n")
                            playagain()

        elif row2path == "2":
            if row3path == "1":
                if row4path == "1":
                    print("\n\nYou started throwing the Deltas' soma out of a window and they attacked you. Your friend Helmholtz joined you in fighting them off while Bernard tried to sneak away, and the police came and arrested you all. You were taken to the World Controller's office, where you and he talk about philosophy, science, and religion. You have done an okay job of aligning yourself with normal behavior within the World State, but you still cannot accept the idea that people can be happy while knowing they are in a lower place than someone else. Your abnormal ideas of equality, relationships, and freedom can cause disorder in this perfectly conditioned society, so the World Controller wants to send you into exile. ")
                    choice = input("You are supposed to go into exile on an island of your choice to be under the World Controller's observation, but you have the ability to run away and live in isolation outside of the civilization. Do you escape?\n1: Yes\n2: No\n\n")
                    if choice == "1":
                        print("\n\nYou escape and go live in an abandoned lighthouse away from people. You are soon discovered, however, and after people pester you and treat you like a zoo animal and you brutally attack Lenina and take soma, you are so distraught with your actions and plagued by your everlasting guilt that you kill yourself.\n")
                        playagain()
                    elif choice == "2":
                        choice = input("\n\nPick an island: \n1: Iceland - it is very cold and remote, but the people there think the most like you and the World Controller views it as a reward.\n2: Samoa - the climate is very warm and tropical (according to the World Controller) and you will probably have an easier life than at any of the other island options.\n3: The Falkland Islands - the climate is very harsh, with heavy winds and storms. You will probably be very unhappy there, but your hardships will inspire you to think and write more. Bernard and Helmholtz will be there as well. ")
                        if choice == "1":
                            print("\nYou will be sent to Iceland.\n")
                            playagain()
                        elif choice == "2":
                            print("\nYou will be sent to Samoa.\n")
                            playagain()
                        elif choice == "3":
                            print("\nYou will be sent to the Falkland Islands.\n")
                            playagain()
                    
                elif row4path == "2":
                    print("\n\nYou have chosen to accept the way the world works. The Deltas are happier if they take soma and don't think about how they have been engineered to not feel real feelings and to enjoy having a horrible job and being stupid and looked down upon by everyone else. You won't get in the way of that. However, due to your upbringing and the rebellious natures of your friends Bernard and Helmholtz, you are taken to the World Controller's office for a talk. You have done a decent job of adapting to the World State's conditioning and behaviors, but you still pose a risk to society should your ideas of Shakespeare and freedom come to light. ")
                    choice = input("You are supposed to go into exile on an island of your choice to be under the World Controller's observation, but you have the ability to run away and live in isolation outside of the civilization. Do you escape?\n1: Yes\n2: No\n\n")
                    if choice == "1":
                        print("\n\nYou escape and go live in an abandoned lighthouse away from people. You are soon discovered, however, and after people pester you and treat you like a zoo animal and you brutally attack Lenina and take soma, you are so distraught with your actions and plagued by your everlasting guilt that you kill yourself.\n")
                        playagain()
                    elif choice == "2":
                        choice = input("\n\nPick an island: \n1: Iceland - it is very cold and remote, but the people there think the most like you and the World Controller views it as a reward.\n2: Samoa - the climate is very warm and tropical (according to the World Controller) and you will probably have an easier life than at any of the other island options.\n3: The Falkland Islands - the climate is very harsh, with heavy winds and storms. You will probably be very unhappy there, but your hardships will inspire you to think and write more. Bernard and Helmholtz will also be there. ")
                        if choice == "1":
                            print("\nYou will be sent to Iceland.\n")
                            playagain()
                        elif choice == "2":
                            print("\nYou will be sent to Samoa.\n")
                            playagain()
                        elif choice == "3":
                            print("\nYou will be sent to the Falkland Islands.\n")
                            playagain()

            elif row3path == "2":
                if row4path == "1":
                    print("\n\nYou started throwing the Deltas' soma out of a window and they attacked you. Your friend Helmholtz joined you in fighting them off while Bernard tried to sneak away, and the police came and arrested you all. You were taken to the World Controller's office, where you and he talk about philosophy, science, and religion. You have refused to conform to normal behavior within the World State, and you cannot accept the idea that people can be happy while knowing they are in a lower place than someone else. Your abnormal ideas of equality, relationships, and freedom are dangerous and can cause disorder in this perfectly conditioned society, so the World Controller wants to send you into exile. Congratulations for making all the same choices that the main character, John, made in the real story. ")
                    choice = input("You are supposed to go into exile on an island of your choice to be under the World Controller's observation, but you have the ability to run away and live in isolation outside of the civilization. Do you escape?\n1: Yes\n2: No\n\n")
                    if choice == "1":
                        print("\n\nYou escape and go live in an abandoned lighthouse away from people. You are soon discovered, however, and after people pester you and treat you like a zoo animal and you brutally attack Lenina and take soma, you are so distraught with your actions and plagued by your everlasting guilt that you kill yourself.\n")
                        playagain()
                    elif choice == "2":
                        choice = input("\n\nPick an island: \n1: Iceland - it is very cold and remote, but the people there think the most like you and the World Controller views it as a reward.\n2: Samoa - the climate is very warm and tropical (according to the World Controller) and you will probably have an easier life than at any of the other island options.\n3: The Falkland Islands - the climate is very harsh, with heavy winds and storms. You will probably be very unhappy there, but your hardships will inspire you to think and write more. Bernard and Helmholtz will be there as well. ")
                        if choice == "1":
                            print("\nYou will be sent to Iceland.\n")
                            playagain()
                        elif choice == "2":
                            print("\nYou will be sent to Samoa.\n")
                            playagain()
                        elif choice == "3":
                            print("\nYou will be sent to the Falkland Islands.\n")
                            playagain()
                    
                elif row4path == "2":
                    print("\n\nYou have chosen to accept the way the world works. The Deltas are happier if they take soma and don't think about how they have been engineered to not feel real feelings and to enjoy having a horrible job and being stupid and looked down upon by everyone else. You won't get in the way of that. However, due to your upbringing and the rebellious natures of your friends Bernard and Helmholtz, you are taken to the World Controller's office for a talk. You haven't done a great job of adapting to the World State's conditioning and behaviors, and you still pose a risk to society should your ideas of Shakespeare and freedom come to light. ")
                    choice = input("You are supposed to go into exile on an island of your choice to be under the World Controller's observation, but you have the ability to run away and live in isolation outside of the civilization. Do you escape?\n1: Yes\n2: No\n\n")
                    if choice == "1":
                        print("\n\nYou escape and go live in an abandoned lighthouse away from people. You are soon discovered, however, and after people pester you and treat you like a zoo animal and you brutally attack Lenina and take soma, you are so distraught with your actions and plagued by your everlasting guilt that you kill yourself.\n")
                        playagain()
                    elif choice == "2":
                        choice = input("\n\nPick an island: \n1: Iceland - it is very cold and remote, but the people there think the most like you and the World Controller views it as a reward.\n2: Samoa - the climate is very warm and tropical (according to the World Controller) and you will probably have an easier life than at any of the other island options.\n3: The Falkland Islands - the climate is very harsh, with heavy winds and storms. You will probably be very unhappy there, but your hardships will inspire you to think and write more. Bernard and Helmholtz will also be there. ")
                        if choice == "1":
                            print("\nYou will be sent to Iceland.\n")
                            playagain()
                        elif choice == "2":
                            print("\nYou will be sent to Samoa.\n")
                            playagain()
                        elif choice == "3":
                            print("\nYou will be sent to the Falkland Islands.\n")
                            playagain()

    
    row6(path[2], path[6], path[10], path[14])

game()
