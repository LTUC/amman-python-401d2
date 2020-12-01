# file = open('assets/spam.txt', 'r')

with open('assets/spam.txt', 'r') as file:
    print('Is the files closed?', file.closed)
    content = file.read()
print('Is the files closed?', file.closed)

content = content + '\nthis is extra\n'
print(content)
# file.close()




# with open('assets/brain.jpg', 'rb') as brain:
#     content = brain.read()

# # for x in content[:50]:
# #     print(x)


# print(len(content))

# with open('assets/brain.copy2.jpg', 'wb') as brain2:
#     brain2.write(content[:10000])


