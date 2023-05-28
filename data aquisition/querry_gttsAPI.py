from gtts import gTTS
import sys, os


translated = 0
total = 0
dataset = sys.argv[1]
for authorId in os.scandir(str(dataset + '/' + 'LibriSpeech' + '/' + dataset)):
    for chapterId in os.scandir(str(authorId.path)):
        for file in os.scandir(str(chapterId.path)):
            if file.name.endswith('_spanish.txt'):
                with open(file, 'r') as infile:
                    for line in infile:
                        splitL = line.split()
                        found = False
                        for word in splitL:
                            if len(word.split('-'))==3:
                                # create words and outfile
                                outfile = word + '.mp3'
                                index = splitL.index(word)
                                words = splitL[0:index] + splitL[index+1:]
                                found = True
                                break
                        if not found:
                            # sanity check
                            sys.exit("config err in " + authorId.name + " in " + chapterId.name)
                        
                        # if translated file exists, skip
                        if os.path.exists(chapterId.path + '/' + outfile):
                            continue
                        
                        text = (' '.join(words))
                        try:
                            audioObj = gTTS(text, lang='es', slow=False)
                        except:
                            sys.exit("error in " + authorId.name + " in " + chapterId.name)
                        audioObj.save(chapterId.path + '/' + outfile)
                translated += 1
            total = total + 1
    print(authorId.name, 'done')
    
print(translated, 'out of', total)
