import random
n_people= int(input("Enter the number of every friend (including you):\n"))
if n_people == 0 or n_people < 0:
    print("No one is joining for the party")
else:
    availabl = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(1,n_people+1):
        freinds_names = input()
        availabl.update({freinds_names:0})
    print("Enter the total bill value:")
    bill_total = input()
    freinds_names = list(availabl.keys())
    bill_total_all = float(float(bill_total) / int(n_people))
    for i in freinds_names:
        availabl.update({i: round(bill_total_all, 2)})
    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    result = input()
    if(result.upper() == "YES"):
        luck = random.choice(freinds_names)
        print("{} is the lucky one!".format(luck))
        for i in freinds_names:
            if i == luck:
                availabl.update({i: 0})
            else:
                bill_total_all = float(bill_total) / float((int(n_people) - 1))
                availabl.update({c: round(float(bill_total_all), 2)})
        print(availabl)
    else:
        print("No one is going to be lucky")
        print(availabl)
