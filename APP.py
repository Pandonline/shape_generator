import form

def pp(tab):
    for line in tab:
        print(' '.join(line))


pp(form.disk(9))
pp(form.circle(9))