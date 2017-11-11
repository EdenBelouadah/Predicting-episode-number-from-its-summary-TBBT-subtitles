from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import  os
import re
from sklearn.feature_extraction import text 
my_stop_words = text.ENGLISH_STOP_WORDS
import gensim
import nltk

##############################
#UNUSED TRIES
#nltk.download('wordnet') # first-time use only
#lemmer = nltk.stem.WordNetLemmatizer()
#def LemTokens(tokens):
#    return [lemmer.lemmatize(token) for token in tokens]
#remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
#def LemNormalize(text):
#    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))    
#
#
#
#stemmer = nltk.stem.porter.PorterStemmer()
#def StemTokens(tokens):
#     return [stemmer.stem(token) for token in tokens]
#remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
#def StemNormalize(text):
#     return StemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
##############################





#A function that returns all the numbers in a string concatenated
def get_num(Str):
    return int(''.join(char for char in Str if char.isdigit()))   
                
#A function that cleans html tags from a string
def cleanhtml(Str):
  cleaner = re.compile('<.*?>')
  cleantext = re.sub(cleaner, '', Str)
  return cleantext


#get similarity between 2 texts using cosinus similarity
def get_similarity(text1, text2, v):
    t1 = v.transform([text1])
    t2 = v.transform([text2])
    return cosine_similarity(t1,t2)

available_seasons=5
number_summaries=0
success_rate=0


for i in range(available_seasons):
    season=[]
    summaries=[]
    seas="Season"+str(i+1)
    summ="summaries"+str(i+1)
    for filename in sorted(os.listdir(seas)):
            stri=seas+"/"+filename
            episode_file = open(stri,"r",encoding='latin-1')
            episode_file=episode_file.readlines()
            episode=""
            #Preprocessing
            for line in episode_file:
                if(not line[0].isdigit() and not line=='\n' and 'Downloaded From' not in line):
                    episode+=line   
            episode=episode.replace('\n', ' ')
            episode=cleanhtml(episode)

            
#            cleanr = re.compile('==.*?==')
#            episode = re.sub(cleanr, '', episode)
#            

            
#            corpus=[episode]  
#            tok_corp= [nltk.word_tokenize(episode) ]       
#            model = gensim.models.Word2Vec(tok_corp, min_count=1)
#            stop=model.wv.doesnt_match(corpus[0].split())
#            episode=[word for word in corpus[0].split() if word not in stop]
#            episode=' '.join(episode)           
            
            season.append(episode)

    tfidf_v = TfidfVectorizer( stop_words='english')
    tfidf_v.fit_transform(season)   
    print("###############SEASON %s###################"%(i+1))        
    for summary_name in sorted(os.listdir(summ)): 
        stri=summ+"/"+summary_name
        summary = open(stri,"r",encoding='latin-1').read()    
        number_summaries+=1             
        #Calcul d'erreur:
        i=-1
        max_sim=-1
        
        
#        corpus=[summary]  
#        tok_corp= [nltk.word_tokenize(summary) ]       
#        model = gensim.models.Word2Vec(tok_corp, min_count=1)
#        stop=model.wv.doesnt_match(corpus[0].split())
#        summary=[word for word in corpus[0].split() if word not in stop]
#        summary=' '.join(summary)
#        
        
        
        for episode in season:
            i+=1
            sim=get_similarity(summary,episode , tfidf_v)
            if sim>max_sim:
                max_sim=sim
                i_best_episode=i
        print("Summary %s predicted as episode %s"%(get_num(summary_name)%100,i_best_episode+1))   
        if(i_best_episode+1==get_num(summary_name)%100):
            success_rate+=1
print("##########################################")
success_rate=success_rate/number_summaries*100
print(r"success rate={:.2f}%".format(success_rate))