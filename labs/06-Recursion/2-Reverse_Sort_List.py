def insert(t, x):
  if not t:
    return [x]
  elif t[0] >= x:
    return [t[0]] + insert(t[1:], x)
  else:
    return [x] + t

def run(src, dst):
    if not src:
      return dst
    else:
      return run(src[1:], insert(dst, src[0]))

inp = input('Enter your List : ').split(',')
lst = [int(i) for i in inp]
print(f'List after Sorted : {run(lst, [])}')