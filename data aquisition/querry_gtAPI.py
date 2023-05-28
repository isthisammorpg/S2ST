from googletrans import Translator
import sys, os

translator = Translator()

translated = 0
total = 0
dataset = sys.argv[1]
for authorId in os.scandir(str(dataset + '/' + 'LibriSpeech' + '/' + dataset)):
    for chapterId in os.scandir(str(authorId.path)):
        for file in os.scandir(str(chapterId.path)):
            if file.name.endswith('_spanish.txt'):
                os.system(f'rm {file.path}')
                continue
            total = total + 1
            if file.name.endswith('.txt'):
                translated += 1
                with open(str(file.path), 'r') as inFile:
                    text = inFile.read()

                # 15k is the translator limit for googletrans
                out_text = []
                for i in range(0, len(text), 1500):
                    out_text.append(translator.translate(text[i:min(i+1500, len(text))], dest='es').text)
                    
                with open(str(chapterId.path + '/' + file.name[:-4] + '_spanish' + '.txt'), 'w') as outFile:
                    outFile.write(''.join(out_text))
    print(authorId.name, 'done')
    
print(translated, 'out of', total)
