def is palindrome(s):
  return s==s[::-1]
  s=input()
  p=is palindrome(s)
  if p:
    print('yes')
  else:
    print('no')
