#day95 regular expressons
'''
METACHARACTERS:
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs

'''
import re

pattern= r"[A-Z]+yclone"
text='''
World Wrestling Entertainment (WWE) is an American professional wrestling promotion. It is owned and operated by TKO Group Holdings, a majority-owned Cyclone-dyclone subsidiary of Endeavor Group Holdings.[9] A global integrated media and entertainment company, WWE has also branched out into fields outside of wrestling, including film, football, and various other business ventures. The company is additionally involved in licensing its intellectual property to companies to produce video games and action figures.
'''
#to find the first occurrence
match=re.search(pattern,text)
print(match)

#to find all occurrences
matches=re.finditer(pattern,text)
for match in matches:
    print(match.span())

    print(text[match.span()[0]:match.span()[1]])
