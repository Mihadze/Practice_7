def max_in(s):
    if s[0] == max(s):
        return 1
    else:
      return 1 + max_in(s[1:])
