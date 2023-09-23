from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

all_symptoms = np.load('wordcloud.npy')


symptom_dict = {}
infile = open('./COVID-Twitter-Symptom-Lexicon.txt')
for line in infile:
    items = line.split('\t')

    symptom_dict[str.strip(items[1])] = str.strip(items[0])

df = pd.DataFrame({
    'symptom_code': all_symptoms
})

df['symptom'] = df['symptom_code'].map(symptom_dict)
df['symptom'] = [symptom.replace(',', '').replace('&', '') for symptom in df['symptom']]

modified_symptoms = [symptom.replace(' ', '_') for symptom in df['symptom']]

text = ' '.join(modified_symptoms)

wordcloud = WordCloud(background_color='white', width=800, height=400).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
