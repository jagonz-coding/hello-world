#Name: Juan Gonzalez
#ID: 1808943

sentence = input()
start = 0
end = len(sentence) - 1

while(start < end):
    if(sentence[start] == ' '):
        start += 1
    elif(sentence[end] == ' '):
        end -= 1
    elif(sentence[start] != sentence[end]):
        print(sentence, "is not a palindrome")
        break
    else:
        start += 1
        end -= 1
        if ((start > end) or (start == end)):
            print(sentence, "is a palindrome")