#problem 1:
def sum_even_numbers(numbers):
    even_sum=0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    print(even_sum)
#sum_even_numbers([1,2,3,4,5,6,7,8,9,10])


#problem 2:
def char_frequency(word):
    frequency={}
    for char in word:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    return frequency
result = char_frequency("hello")
#print(result)

#problem 3:
def filter_negative_numbers(numbers):
    negative_numbers=[num for num in numbers if num >=0]
    print(negative_numbers)
#filter_negative_numbers([-1,0,2,-3,5])

#problem 4:
def average_score(grades):
    total_grades=sum(num for num in grades.values() if isinstance(num,(int,float)))/len(grades)
    print(total_grades)
#average_score({'Alice':85, 'Bob':90, 'Charlie':78})

#problem 5:
def reversed_list(numbers):
    list_reversed=list(reversed(numbers))
    print(list_reversed)
#reversed_list([1,2,3])

#problem 6:
def count_vowels():
    words=input("Please provied a phrase or word: ")
    print(words)
count_vowels()