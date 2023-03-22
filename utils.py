import numpy as np
import json
import pickle

class CapexPredection():
    def __init__(self,data):
        self.data = data
        print(self.data)

    def __loading(self): # private method      
        """
        Pickle & JSON file importing
        """

        with open('artifacts/project_data.json','r') as file:
            self.project_data = json.load(file)  
                                        
        with open("artifacts/model.pkl",'rb') as file:
            self.model = pickle.load(file)



    def Fiber_Capex_Predection(self):
        """
        Fiber_Capex_Predection
        """
        self.__loading()

        TND_Scope_IP_Meter =  self.data['html_TND_Scope_IP_Meter']
        TND_per_Meter =  self.data['html_TND_per_Mete']
        ROW_Per_Meter =  self.data['html_ROW_Per_Meter']
        ID = self.data['html_ID']
        state = self.data['html_state']

        user_data = np.zeros(len(self.project_data['column_names']))
        user_data[0] = TND_Scope_IP_Meter
        user_data[1] = TND_per_Meter
        user_data[2] = ROW_Per_Meter
        user_data[3] = user_data[0] * user_data[1]
        user_data[4] = user_data[0] * user_data[2]
        user_data[5] = 45154+(user_data[0]*1.1*3657)+(user_data[0]*1.1*200)+(((user_data[0]/200)+1)*3745)+(((user_data[0]/200)+1)*5744)
        user_data[6] = 47500
        user_data[7] = 33933
        user_data[8] = 19413
        user_data[9] = 900                    
                                           
        BLDG_ID = 'BLDG_ID_'+ID
        index = np.where(np.array(self.project_data['column_names']) == BLDG_ID)[0]
        user_data[index] = 1

        R4G_State = 'state_'+state
        index = np.where(np.array(self.project_data['column_names']) == R4G_State)[0]
        user_data[index] = 1



        return self.model.predict([user_data])[0]      