import pandas as pd
import joblib


class ML_D11:
    MODEL = 'ML-D11'

    def __init__(self):
        self.data = None
        self.model_pipeline = joblib.load('ML-D11-pipeline.joblib')
    
    def predict(self, temp=None, crit_vol=None, crit_temp=None, dens=None, acent_fact=None ):
        data_dict = {
            'T': temp,
            'Vc': crit_vol,
            'Tc': crit_temp,
            'dens': dens,
            'w':acent_fact
        }
        self.data_df = pd.DataFrame.from_dict(data_dict)
        return 10**(self.model_pipeline.predict(self.data_df))
    
    

