import re

dingdong ='''
 WikipediaThe Free Encyclopedia

View history
 
 This is a good article. Click here for more information.
Page semi-protected
From Wikipedia, the free encyclopedia
For other uses, see Dog (disambiguation).
"Doggy" and "Pooch" redirect here. For other uses, see Doggy (disambiguation) and Pooch (disambiguation).
Dog
Temporal range: 0.0142–0 Ma 
PreꞒꞒOSDCPTJKPgN
Late Pleistocene (14,200 years ago) to present[1]



A Golden Retriever.
A black Labrador Retriever.



Conservation status
Domesticated
Scientific classification Edit this classification
Kingdom:	Animalia

Synonyms[3]
List
The dog (Canis familiaris or Canis lupus familiaris) is a domesticated descendant of wolves. Also called the domestic dog, it was selectively bred during the Late Pleistocene by hunter-gatherers. Dogs and the modern gray wolf share a common ancestor.[4] Dogs were the first species to be domesticated over 14,000 years ago, before the development of agriculture,
'''
#findall, search, split, sub, finditer
patt = re.compile(r'over')
patt = re.compile(r'.be') 
patt = re.compile(r'^years') 
patt = re.compile(r'ture$') 
patt = re.compile(r'ai*')
patt = re.compile(r'ai+')
patt = re.compile(r'ai{2}')
patt = re.compile(r'(ai){2}')
patt = re.compile(r'ai{2}|t')

#Special sequences
patt = re.compile(r'\Ayears')
patt = re.compile(r'\byears')
patt = re.compile(r'years\b')
patt = re.compile(r'14\b')
patt = re.compile(r'\d{5}-\d{14}')


matches=patt.finditer(dingdong)
for match in matches:
    print(match)



    print(dingdong[888:892]) #<re.Match object; span=(888, 892), match='over'> over
#print(r"\n") --->escape sequence ko regulary escape nhi krta hai...




#CHALLANGE-->

#Given a string with a lot of indian phone numbers string from +91