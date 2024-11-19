f = open('colored.svg', 'r')
txt = f.read()
f.close()

txt = txt.replace('d=', 'stroke-width="4" d=')
print(txt)