str = input('Enter a string: ')
dict = dict()

def most_frequent(str):
     for i in str:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
     print(dict)

most_frequent(str)
