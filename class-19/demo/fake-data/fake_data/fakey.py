from faker import Faker

# fake = Faker('ar_SA')
fake = Faker()



# print(dir(fake))
# print(fake.country())
# print(fake.name())
# print(fake.address())


text = ''
for i in range(100):
    text += fake.paragraph()
    text += fake.name() + " "
    text += fake.paragraph() + " "
    text += fake.phone_number() + " "
    text += fake.paragraph() + " "
    text += fake.email() + '\n\n'


with open('fake_text.txt', 'w+') as f:
    f.write(text)



import shutil
shutil.copy('fake_text.txt', '..')
