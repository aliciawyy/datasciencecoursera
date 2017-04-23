text = raw_input().strip().split(' ')
num = int(raw_input())
keywords = set(raw_input().strip().split(' '))

for i in range(len(text)):
    if text[i] in keywords:
        text[i] = "<b>{}</b>".format(text[i])

print ' '.join(text)
