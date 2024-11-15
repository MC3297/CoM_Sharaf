f = open("trollface.svg", "r")
txt = f.read().replace(" Z ", '"/></g>\n<g><path style="opacity:0.981" fill="#FFFFFF" d="')
o = open("edited.svg", "w")
o.write(txt)