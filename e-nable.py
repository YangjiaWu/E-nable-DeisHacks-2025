import pandas as pd

metadata = ['Field Name Data type (how to sort or search?)','Model name (or Product Name?)','Affiliated Organization','Country of Origin (or Location?)','Designer ID',
            'Designer Name','License Name', 'STL Files', 'Source CAD Files','Origin','Details','Instructions','Assembly Materials Kit',
            'Video Tutorials','Ename Device Color','Date Modified','Date first uploaded?','Maturity','Cost of materials',
            'Popularity','Difficulty','Grip Strength','Last date Modified','e-Nable Device link','Device Photo',
            'Device Description','Link to Device','Device Link']

dictionary = {title: [] for title in metadata}

# print(dictionary)

# not_found = 0
# dictionary[not_found] = []
with (open("raw text.txt", "r") as file):

    prev = metadata[0]
    category = metadata[0]
    for line in file:

        # see if any of the strings in the list are in the metadata
        found = False
        for string_cat in metadata:
            if string_cat in line:
                if((string_cat != "Origin" or metadata[3] not in line) and (string_cat != "Instructions" or " Instructions" not in line)):
                    category = string_cat
                    found = True
                if(string_cat == metadata[0]):
                    for key in dictionary:
                        if len(dictionary[key]) != len(dictionary[metadata[0]]):
                            dictionary[key].append("")
        if found:
            #category = ... # the data that was found
            print(f"putting {line} in {category}")

            dictionary[category].append(line[len(category)+1:])
            prev = category

        # else, put into the previous
        else:
            print(prev)
            dictionary[prev][-1] += line

            # .append(line)
    for key in dictionary:
        if len(dictionary[key]) < len(dictionary[metadata[0]]):
            dictionary[key].append("")


        print(line)
      #  if line.startswith(metadata[not_found]):
      #      dictionary[not_found].append(line)
            # index += 1
       # elif not_found != 0:  #
        #    dictionary[not_found].append(line)

for key in dictionary:
    print({key:len(dictionary[key])})
    print({key: dictionary[key]})


df = pd.DataFrame.from_dict(dictionary)
df.to_csv("DeisHacks.csv", index=False)
