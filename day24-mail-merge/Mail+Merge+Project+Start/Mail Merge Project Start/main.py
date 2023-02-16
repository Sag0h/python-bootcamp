#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"day24-mail-merge\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt", mode= "r") as file:
    letter = file.read()

with open(r"day24-mail-merge\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt", mode= "r") as file:
    names = file.read()

names = names.split("\n")

for name in names:
    with open(r"day24-mail-merge\Mail+Merge+Project+Start\Mail Merge Project Start\Output\ReadyToSend\letter_for_"+name+".txt", mode="w") as file:
        file.write(letter.replace("[name]", name))
