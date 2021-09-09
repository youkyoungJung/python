def isPalindrome(s: str):
    strs:Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

if __name__ == "__main__":
    print(isPalindrome("race a car"))

