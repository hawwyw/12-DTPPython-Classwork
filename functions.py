func = int(input("Enter what function yo want: "))

if func == 1:
    def adding(num1,num2):
        total=num1+num2
        return total

    total = adding(57,9)
    print(total)
elif func == 2:
    def highest(list_num):
        list_num.sort()
        high = list_num[len(list_num) -1]
        return high

    num_list = [1, 2, 3, 5, 3, 6, 1]
    high = highest(num_list)
    print(high)
elif func == 3:
    def vowels(string_here):
        no_of_vowels = 0
        for i in range(len(string_here)):
            if string_here[i] == "a" or string_here[i] == "e" or string_here[i] == "i" or string_here[i] == "u" or string_here[i] == "o":
                no_of_vowels += 1
        return no_of_vowels

    string_here = str(input("Enter a string here: "))
    no_of_vowels = vowels(string_here)
    print(no_of_vowels)
elif func == 4:
    def true_or_false(str1, str2):
        if str1 == str2:
            same = "True"
        else:
            same = "False"
        return same

    str1 = str(input("ENTER string here: "))
    str2 = str(input("ENTER string here: "))

    same = true_or_false(str1, str2)
    print(same)

elif func == 5:
    def long_strings(string_list):
        for i in range(string_list):
            if len(string_list[i]) > 3:
                new_list.append(string_list[i])
        return new_list