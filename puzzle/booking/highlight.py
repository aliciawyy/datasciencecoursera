text = raw_input().strip().split(' ')
num = int(raw_input())
keywords = set(raw_input().strip().split(' '))


for word in text:
    if word in keywords:
        print "<b>{}</b>".format(word),
    else:
        print word,
