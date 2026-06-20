print("=== Word Frequency Counter===")

text = input("paste your text here : ")

text_split =text.split()
text_split = [word.lower() for word in text_split]


counts ={}
print("Word Frequencies (most common first) :")

for word in text_split:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

sorted_text = sorted(counts.items(), key= lambda x:x[1], reverse=True)
for word,count in sorted_text:


    print(f"{word} :{count}")

total_words = len(text_split)
total_counts = len(sorted_text)

print(f"Total words: {total_words}")
print(f"Total Unique words: {total_counts}")

while True:

    search_word =input("search for a word or type quit to exit : ")
    search_word = search_word.lower()

    if search_word == "quit":
        break
    elif search_word in counts:

        print (f"{search_word} appears {counts[search_word]} times")
    else:
        print("No such word found")

print("goodbye")        