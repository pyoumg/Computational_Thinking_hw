word=input('단어를 입력하시오 : ')
old_word=word
word=list(word)
print(word)
word[0:0]=['a','n','t','i']
print(word)
word=list(word[len(word)-1])+word[0:len(word)-1]
print(word)
print(old_word,'==>',''.join(word))
