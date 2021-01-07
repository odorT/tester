from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
strng=input()
if(check(strng)==True):
      print("pangram")
else:
      print("not pangram")
