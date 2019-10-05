def ispalindrome(data):
    return data==data[::-1]

data=input("Please provide a word :")
print(f"Data {data} is palindrome : {ispalindrome(data)}")