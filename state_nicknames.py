import random

state_dict =	{
	"Alabama":	"Yellowhammer State",
	"Alaska":	"The Last Frontier",
	"Arizona":	"The Grand Canyon State",
	"Arkansas":	"The Natural State",
	"California":	"The Golden State",
	"Colorado":	"The Centennial State",
	"Connecticut":	"The Constitution State",
	"Delaware":	"The First State",
	"Florida":	"The Sunshine State",
	"Georgia":	"The Peach State",
	"Hawaii":	"The Aloha State",
	"Idaho":	"The Gem State",
	"Illinois":	"The Prairie State",
	"Indiana":	"The Hoosier State",
	"Iowa":	"The Hawkeye State",
	"Kansas":	"The Sunflower State",
	"Kentucky":	"The Bluegrass State",
	"Louisiana":	"The Pelican State",
	"Maine":	"The Pine Tree State",
	"Maryland":	"The Old Line State",
	"Massachusetts":	"The Bay State",
	"Michigan":	"The Great Lakes State",
	"Minnesota":	"The North Star State",
	"Mississippi":	"The Magnolia State",
	"Missouri":	"The Show Me State",
	"Montana":	"The Treasure State",
	"Nebraska":	"The Cornhusker State",
	"Nevada":	"The Silver State",
	"New Hampshire":	"The Granite State",
	"New Jersey":	"The Garden State",
	"New Mexico":	"The Land of Enchantment",
	"New York":	"The Empire State",
	"North Carolina":	"The Tar Heel State",
	"North Dakota":	"The Peace Garden State",
	"Ohio":	"The Buckeye State",
	"Oklahoma":	"The Sooner State",
	"Oregon":	"The Beaver State",
	"Pennsylvania":	"The Keystone State",
	"Rhode Island":	"The Ocean State",
	"South Carolina":	"The Palmetto State",
	"South Dakota":	"Mount Rushmore State",
	"Tennessee":	"The Volunteer State",
	"Texas":	"The Lone Star State",
	"Utah":	"The Beehive State",
	"Vermont":	"The Green Mountain State",
	"Virginia":	"The Old Dominion",
	"Washington":	"The Evergreen State",
	"West Virginia":	"The Mountain State",
	"Wisconsin":	"The Badger State",
	"Wyoming":	"The Equality State"
}

num_correct = 0

def test(num_correct):
	question = random.choice(list(state_dict.keys()))
	real_answer = state_dict.get(question)
	print(question)
	nickname = raw_input("Give the nickname for the above state: ")
	if nickname.lower() not in real_answer.lower() or nickname is '' or nickname is None:
		print("Wrong! Correct answer is: % s"% real_answer)
		return num_correct
	else:
		print("Correct")
		num_correct += 1
		return num_correct

while num_correct < 10:
	print("% s / 10")% num_correct	
	num_correct = test(num_correct)

print("Well done! You know your state nicknames!")
