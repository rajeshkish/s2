p=str(input())
if (p=='a' or p=='A' or p=='e' or p=='E' or p=='i' or p=='I' or p=='o' or p=='O' or p=='u' or p=='U'):
    print('Vowel')
elif (p>='a' and p<='z') or (p>='A' and p<='Z'):
    print('Consonant')
else:
    print('invalid')
