import pickle
import numpy as np
import json
import config


class Mobileprice():
    def __init__(self):
        pass
    
    def get_data(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model=pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_d = json.load(f)

    def get_predicted_mobileprice(self,System,Memory,RAM,Display,Display_Quality,Camera,Battery,Sim,Screen_Refresh_Rate, Make):

        self.get_data()
    
        System=self.json_d["System"][System]
        Memory = self.json_d["Memory"][Memory]
        RAM = self.json_d["RAM"][RAM]
        Display = self.json_d["Display"][Display]
        Display_Quality= self.json_d["Display_Quality"][Display_Quality]
        Camera = self.json_d["Camera"][Camera]
        Battery = self.json_d["Battery"][Battery]
        Sim = self.json_d["Sim"][Sim]
        Screen_Refresh_Rate= self.json_d["Screen_Refresh_Rate"][Screen_Refresh_Rate]
        Make = "Make_" + Make
        Make_index = self.json_d["Column_names"].index(Make)
        

        test_array=np.zeros([1,self.model.n_features_in_])
        
        test_array[0,0] = System
        test_array[0,1] = Memory
        test_array[0,2] = RAM
        test_array[0,3] = Display
        test_array[0,4] = Display_Quality
        test_array[0,5] = Camera
        test_array[0,6] = Battery
        test_array[0,7] = Sim
        test_array[0,8] = Screen_Refresh_Rate
        test_array[0,Make_index] = 1

        predicted_price = self.model.predict(test_array)[0]
        return predicted_price


