import sys
from PyQt5 import QtWidgets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import design
import os 
import re

class ExampleApp(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        # initialisation des objets de l'interface graphique
        self.run_button.clicked.connect(self.run_fun)
        self.clear_button.clicked.connect(self.clear_fun)
        self.load_summary_button.clicked.connect(self.load_summary_fun)
        self.season_combo_box.activated.connect(self.load_season_fun)
        self.season_combo_box.addItem("Season1")
        self.season_combo_box.addItem("Season2")
        self.season_combo_box.addItem("Season3")
        self.season_combo_box.addItem("Season4")
        self.season_combo_box.addItem("Season5")
        self.season_combo_box.addItem("All seasons")
        #Variables initialization        
        global seasons
        global available_seasons
        global right_summary_number
        global tfidf_vects
        seasons=[]
        available_seasons=['Season1','Season2','Season3','Season4','Season5']
        tfidf_vects=[]
        right_summary_number=-1
        self.load_season_fun()
        
        
    #A function that shows a message in the graphical interface       
    def showMessage(self,typeMsg,message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(typeMsg)
        msg.exec_()
    
     #A function that runs the inference on the resume   
    def run_fun(self):
        global available_seasons
        global seasons
        global tfidf_vects
        global right_summary_number
        global right_season_number

        if (self.summary_text.toPlainText()==""):
            self.showMessage("Error!","You must load a summary!")
        else:
            #Get the summary text
            summary=self.summary_text.toPlainText()
            max_sim=-1
            j=-1
            for season in seasons:
                i=-1
                j+=1
                for episode in season:
                    i+=1
                    #Calculate the similarity between the summary and all the episodes
                    sim=self.get_similarity(summary, episode, tfidf_vects[j])
                    #Update the best similar episode
                    if sim>max_sim:
                        max_sim=sim
                        i_best_episode=i
                        i_best_season=j
            
            #When the system can't fine the answer
            if(max_sim==0):
                answer="None -> (Wrong answer)"
            else:
                #Otherwise
                chosen_season=self.season_combo_box.currentText()  
                if(chosen_season=='All seasons'):
                    answer="Season %s - Episode %s"% (i_best_season+1, i_best_episode+1)
                    if(right_summary_number==i_best_episode+1 and right_season_number==i_best_season+1):
                        answer+=" -> (Correct answer)"
                    else:
                        answer+=" -> (Wrong answer)"
                
                else:
                    answer="Season %s - Episode %s"% (self.get_num(chosen_season), i_best_episode+1)
                    if(right_summary_number==i_best_episode+1 and right_season_number==self.get_num(chosen_season)):
                        answer+=" -> (Correct answer)"
                    else:
                        answer+=" -> (Wrong answer)"
            
            #Return the best answer found
            self.episode_text.clear()
            self.episode_text.setText(answer)
            
     #Afunction that returns all the numbers in a string concatenated   
    def get_num(self,Str):
        return int(''.join(char for char in Str if char.isdigit()))

    #A function that erases the summary and the enswer from the graphical interface    
    def clear_fun(self):
        self.summary_text.clear()
        self.episode_text.clear()
                        
    #get similarity between 2 texts using cosinus similarity
    def get_similarity(self,text1, text2, v):
        t1 = v.transform([text1])
        t2 = v.transform([text2])
        return cosine_similarity(t1,t2)
    
    def cleanhtml(self,Str):
        cleaner = re.compile('<.*?>')
        cleantext = re.sub(cleaner, '', Str)
        return cleantext
    
    #A function that loads exactly one season s
    def load_season(self, s):
        #Get the episodes
        season=[]
        for filename in sorted(os.listdir(s)):
                stri=s+"/"+filename
                episode_file = open(stri,"r",encoding='latin-1')
                episode_file=episode_file.readlines()
                episode=""
                for line in episode_file:
                    #preprocessing
                    if(not line[0].isdigit() and not line=='\n' and 'Downloaded From' not in line):
                        episode+=line     
                        
                episode=episode.replace('\n', ' ')
                episode=self.cleanhtml(episode)        
                season.append(episode)
        return season
        

    #A function that loads the chosen season 'or all seasons) chosen by the user
    def load_season_fun(self):
        global seasons
        global tfidf_vects    
        seasons=[]
        tfidf_vects=[]
        chosen_season=self.season_combo_box.currentText()
        if(chosen_season=='All seasons'):
            for s in available_seasons:
                season=self.load_season(s)
                seasons.append(season)
                #Learning the model
                tfidf_v = TfidfVectorizer( stop_words='english')
                tfidf_v.fit_transform(season)   
                tfidf_vects.append(tfidf_v)
        else:
            season=self.load_season(chosen_season)
            seasons.append(season)
            tfidf_v = TfidfVectorizer( stop_words='english')
            tfidf_v.fit_transform(season)   
            tfidf_vects.append(tfidf_v)
        

         
    #A function that loads a summary            
    def load_summary_fun(self):
        global right_summary_number
        global right_season_number

        self.clear_fun()
        path=QtWidgets.QFileDialog.getOpenFileName()[0]
        if(path!=''):
            summary=open(path,'r').read()
            self.summary_text.append(summary)      
            number=self.get_num(path)
            right_season_number=number//1000
            right_summary_number=number%100        

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()                
    form.show()                      
    app.exec_()                        
if __name__ == '__main__':             
    main()