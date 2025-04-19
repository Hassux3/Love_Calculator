# Love Calculator by Hassan

print("\tLove Calculator\n")

true = 'true'
love = 'love'

def start():
    #input two names
    name1 = input("Enter your name: ")
    name2 = input("Enter his/her name: ")
    
    #lowering both names
    lower_name1 = name1.lower()
    lower_name2 = name2.lower()
    
    #concatenating both names
    concatenated_name = lower_name1 + lower_name2
    
    #looking for 'true' in concatenated_name
    true_counted = []
    for char in true:
        counted = concatenated_name.count(char)
        true_counted.append(counted)

    #looking for 'love' in concatenated_name
    love_counted = []
    for char in love:
        counted = concatenated_name.count(char)
        love_counted.append(counted)

    true_counts = true_counted[0] + true_counted[1] + true_counted[2] + true_counted[3]
    love_counts = love_counted[0] +  love_counted[1] +  love_counted[2] +  love_counted[3]
    love_score = int(str(true_counts) +str(love_counts))

    if love_score < 10 or love_score > 90:
        print("\nYour love score is", love_score, "and you go together like coke and mentos.")
    elif love_score >= 40 and love_score <= 50:
        print("\nYour love score is", love_score, "and you are alright together.")
    else:
        print("\nYour love score is", love_score)

start()