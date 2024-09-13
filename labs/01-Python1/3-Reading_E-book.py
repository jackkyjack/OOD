print('*** Reading E-Book ***')
text, highlight = input('Text , Highlight : ').split(',')
ans = text.replace(highlight,f"[{highlight}]")
print(ans)