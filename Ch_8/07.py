l = ["apple", "mango", "banana", "tomato"]


def remove_words():
    print("Your Options are : ")
    for i in l:
        print(i, end=", ")

    print("")

    word = input("Enter your choice : ")
    for i in l:
        striped = i.lstrip()
        if(striped == word):
            removed_word = l.remove(i).lstrip()

    return (removed_word)


print(remove_words())
