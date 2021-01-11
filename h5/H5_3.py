word_cards = [['economics','communications','philosophy','history','sociology','psychology'],

['germany','taiwan','korea','china','canada','brazil','spain','turkey','jordan','morocco','egypt'],

['architect','actor','engineer','accountant','baker','dentist','teacher','writer']]

 

word_category = ['학과','국가','직업']

num=int(input('단어 카드 종류를 선택하시오(학과:1, 국가:2, 직업:3) : '))
name=input('{} 이름을 영어로 입력하시오 : '.format(word_category[num-1]))
if name in word_cards[num-1]:
    print('{}은(는) {} 목록에 있습니다.'.format(name,word_category[num-1]))
else:
    print('{}은(는) {} 목록에 없습니다.'.format(name,word_category[num-1]))