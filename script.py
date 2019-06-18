import spacy
import pt_core_news_sm

nlp = pt_core_news_sm.load()
import pandas as pd
import re
import string

csv = pd.read_csv('data/non_tagged/filtered.csv')
# remove links
clean = [re.sub(r"http\S+", "", text) for text in csv['text']]

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
# remove emojis
clean = [emoji_pattern.sub(r'', text) for text in clean]
#troca pontuacao por espaço
clean = [re.sub(r'[^\w\s]',' ',text) for text in clean]
# troca esse caracter especial por espaço
clean = [text.replace(u'\xa0', u' ') for text in clean]
# troca quebra de linha por espaço
clean = [text.replace('\n', ' ') for text in clean]
# remove espaços duplos entre palavras
clean = [' '.join(text.split()) for text in clean]
# remove espaços do inicio e do final da sentença
clean = [text.strip() + '.' for text in clean]
conll = open('data/tagged/test_conll_file.conll',"w+")
for text in clean:
    doc = nlp(text)
    tokens = [(token.orth_, token.lemma_, token.pos_) for token in doc]
    for i in range(len(tokens)):
        array_line = [i+1, tokens[i][0], tokens[i][1].lower(), tokens[i][2],'-','-','-','-','-','*']
        line = '\t'.join([str(x) for x in array_line])
        conll.write(line)
        conll.write('\n')
    line = '\t'.join([str(x) for x in array_line])
    conll.write(line)
    conll.write('\n')
    conll.write('\n')
conll.close()
