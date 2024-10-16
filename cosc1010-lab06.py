# Brian Foster
# UWYO COSC 1010
# Submission Date: 10/15/24
# Lab 06
# Lab Section: 11
# Sources, people worked with, help given to: 
# Ian Catchpole (my girlfriends father)
# ChatGPT (for explaining and providing examples)
# Microsoft bing (for explaining and providing examples)
# PythonForBeginners (for explaining how to "Use A Python Dictionary to Count Occurrences of Each Character in a String")


random_string = """
jppamiqxegokaizvkyawwurhewtcxohryzptznyuedhhmawpic
pkzwuiorngdfcsgqnlyifzyaivehpiyszykqprbcsobygzhadd
yfddbulxmcnyvqhesmnybyuhxjqqmhdxwhcselasiayqhctnlw
hakethjahqnvjdowhlyzosemxkbenestxgvgncmffkcxldcmkl
itclmqdhrbdgzwtvdxwedcknbyaecvttjphtxubvhwvcvjqayy
almxuxjbcmznnzekptfzbldsjwpvringlmalwufvlppeiendur
dyophftqjkghhncwxoksqaqnpueudpygiytqgpcgjqsjbtbpzi
vaeczmyicnednjjoxkpnjmpfbgyjnbfjlweqqppodfxfzzwkuf
rldgryyhceuikimoavosuzuozthmatcgxcmkxnaxmsevkcumby
spiajlbycvrluxdkfavxidzalxuixqkxiybhfuqhcvmrhzbzse
idjwgwdwgfkyreozkyoxdvhixfejxjfgkkgobescboyfshiovu
fxdyvfsnmjzsphgmtldlaoehofcspzujghcdcxzggvunpbtglr
topplmkviuewwpoaplmbpgejmymxbyzzwbnujrlysszmxkjerb
zpiewqvgopvhmmcgwcyvxvwhdvfgsrybcozhdtwujhdbxzznkc
ergcqbetpgwrejuluqfxchlihunzbcdwboysjqenjxzbgqbycx
dybxpyztjyxpkqfvxullzkedpkjjobhymfinpvprxejktyrpai
ehjgwahpquzcmvclatdfcmattavoehnhnzveoxwnmnptxbvxto
gpcobgzdhsjevhcohkltftmrqkosknkxeylhqxkkctbnusijgr
uvecpbqmylqdaohkfaqbgeokyyipumjuaaayikdzyxfrpaieyo
uxiosjwioebsjtslblfurgcodtyaggzovzfnnyjngawiwbbtqi
kqqhnkwheolpqzasmsmbxqkeiqvogquobphewznfsnlkkizhca
cbiyvxpmjxywqvzqtshfvnfbusphggexfqzepsrduvtovdsknl
ztyuwugprkhbmktfvrenbmqgdjwnkeugtojrpqfmjhtrlcqcpq
pwsguedzgvktpwbqkhkueymjtxbvzmdfjopzkygujrjdtogssg
cxczryuqhhgjlpultkoffescpzyjrfqqabnhkfdnhkylpjamxk
uxidjkqdrkxqjqjtflebvwhcvqjciykzhrvppvxhvpedgznwty
kujglixooczrhxziasjxddfcghzlwrqcyiilpruhdfvitewxzg
dzcvmvnoskchscgoqfsojfvahlwkrslzeirlblseplcmpmbmum
ibrdamvqfstydtjopdkdcbnnmpifxckozyxzluhcqbqtpismog
ulufaajxvuizvdzioxfvypxovptkibcrjvfidomejknuggfrtp
kptwffersvqjknemkejsgspckwqisdcliuezhbeqpwgrjcqajl
huobykkbujmyuuinbwdklqfhvakyozzsxghfyownjjwqtkxgkf
ipdbjzxfogozstfsektujsvklrvecditiectuvtfibohmxxzna
cpqzeoburtquuizhypugnkvuwbdxnraareqkofhfjobrpcsuxq
nbafxlkuafbfsiuyrxdusqyasqyrwhdjrukgxdackumvairlgn
fjhenwbrdghbevgqbybpwncclolgqyuhallbqtzdywbvlzwtil
jctmsxjortnxvlbhuhkblppewjhqjzxrwgftlturxjuwfoaqpp
sgfnxwxolkbrpdmpniitoljzaxabgtnelrmryetxqypwrjdyjc
zipwbdpbazxpesmrcfuikeamtlsrgxrhzfytecenyydeemrhxj
gmdruhillntvpadzbroyygydpmonwuakruvxbdrqhtrjvoqsin
gjbarzvuqplmsmbwtqfghteoknbxmaokwlqqfoblmzsxczjzfj
mzmawtarjdtgongqqufhhdjwcinhlxcsgoltjycxrkloqozxoi
crlfmgflzzxgiiliqlksxyaydsohhahzxtsufzppftvgbpsdlx
ertfmbothijzrrdvfrnsohnwulcxvcvxngvmznhazxrgdsugij
fracotpirvqemsiuualpkpvtmtgchmowkmvoolrjfblrtwkmtr
xhawucytgwlahddkhxxfublukkdldpovqokntydhzzrxiisdwu
ujrkoewqoflyebogbwgdhriwkkoiofwtjlhxxtmzkklzbcmxhv
lrslowamkcwolbcgfkfciegdwqskuazxnycqkkggzsowcmafay
ibmkdwkqmdkjesqnjiqpijixbwjhenmsrrlpcseliiajlvcaac
zkdenxczyooloczcaahnkehbwimvieedpdlqfafbqvxvfmvabd
"""
random_string = random_string.replace("\n","") #remove all newline characters
print(len(random_string)) # Print out the size for reference 

# Above is a string with 2500 characters.
# Create a program that goes through and counts the occurrence of each character, excluding \n using a  dictionary ✅
# Output each letter and its corresponding occurrence in alphabetical order ✅
# Output which letter occurred the most ✅
# Output which letter occurred the least ✅
# Output what the percentage of the string each character is, again in alphabetical ✅

#Tips and trick:
# You can iterate through strings like you would a list
# All characters are lowercase 
# Each letter will be PAIRED with its corresponding value 
# That is to say, this is a great use of dictionaries
    # You will  need to add the letter to the dictionary on first occurrence 
    # Then increment its corresponding count 


#Load all the elements into a dictionary
#Will need to first declare a dictionary 

# Output: each letter and its corresponding occurrence in alphabetical order

countOfChars = dict()
for character in random_string:
    if character in countOfChars:
        countOfChars[character] += 1
    else:
        countOfChars[character] = 1
sorted_countOfChars = dict(sorted(countOfChars.items()))
print("The count of characters in the string is:")
print(sorted_countOfChars)
#pythonforbeginners. (2024, Oct. 15-16 (late night)) "how do I Create a program that goes through and counts the occurrence of 
# each character, excluding \n using a dictionary in alphabetical order in python" Found through the link https://www.pythonforbeginners.com/basics/count-occurrences-of-each-character-in-string-python#htoc-count-occurrences-of-each-character-in-a-string-using-a-python-dictionary
print("*"*75)
# Output which letter occurred the most 
def most_frequent_letter(random_string):
    return max(set(random_string), key=random_string.count)
print(most_frequent_letter(random_string))

most_occurred = "k"
def least_frequent_letter(random_string):
    return min(set(random_string), key=random_string.count)
print(least_frequent_letter(random_string))
#Lines 102-109
#Microsoft Bing. (2024, Oct. 15-16 (late night)) "how do i find the most occurred letter in a string in python" 
# Found through the link https://www.bing.com/search?pglt=41&q=how+do+i+find+the+most+occurred+letter+in+a+string+in+python&cvid=16f38af0654d4eecac3b2c65d07131c6&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTE4MTQxajBqMagCALACAA&FORM=ANNTA1&PC=HCTS
least_occurred = "n"

print(f"The letter that occurred the most is: {most_occurred}")
print("*"*75)
# Output which letter occurred the least 
print(f"The letter that occurred the most is: {least_occurred}")
print("*"*75)

# Output what the percentage of the string each character is, again in alphabetical
total_length = len(random_string)
percentages = {char: (count / total_length) * 100 for char, count in sorted_countOfChars.items()}

print("Character percentages:")
for char, percentage in percentages.items():
    print(f"{char}: {percentage:.2f}%")
#Ian Catchpole. (2024, Oct. 15-16 (late night)) "I have to figure out how to make what is in the terminal 
#into percentages, how would I go by in doing so"
#Response was: An example I know of would be using 'a' = 86 and dividing 86 by 2500, and then times that by 100 to 
#equal 3.44%

#this and asking chatgpt helped me figure out what to write down for the code
#chatgpt 4o mini. (2024, Oct. 15-16 (late night)) "example of an output of the percentage of a string each character is" 
#generated using OpenAI. https://chat.openai.com/”