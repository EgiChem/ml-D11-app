import pandas as pd
import joblib


class ML5_D11:
    MODEL = 'ML5-D11'

    def __init__(self):
        self.data = None
        self.model_pipeline = joblib.load('ML5-D11-pipeline.joblib')
    
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
    
    
class ML8_D11:
    MODEL = 'ML8-D11'

    def __init__(self):
        self.data = None
        self.model_pipeline = joblib.load('ML8-D11-pipeline.joblib')
    
    def _get_RDKit_descriptors(self):
        from rdkit import Chem
        from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator

        # Add RDKit mol objects
        self.data_df['mol'] = [Chem.MolFromSmiles(smi) for smi in self.data_df['canonical_smiles'].to_list()]

        DESCRIPTORS = ['NHOHCount', 'NumRotatableBonds']
        desc_calc = MolecularDescriptorCalculator(DESCRIPTORS)
        
        mols = list(self.data_df['mol'])
        
        descriptors = []
        for mol in mols:
            mol_desc = desc_calc.CalcDescriptors(mol)
            descriptors.append(list(mol_desc))
        #int(descriptors)
        df_rdkit = pd.DataFrame(descriptors, columns=DESCRIPTORS)

        # Merge descriptors with the main df
        self.data_df = pd.concat([self.data_df, df_rdkit], axis=1)

        # Remove irrelevant columns
        self.data_df = self.data_df.drop(columns=['canonical_smiles', 'mol'])
        temp = self.data_df['P']
        self.data_df.drop(columns=['P'], inplace=True)
        self.data_df.insert(6, 'P', temp)

        

        return self.data_df


    def predict(self, temp=None, crit_vol=None, crit_temp=None, dens=None, acent_fact=None, press=None, smiles=None ):
        data_dict = {
            'T': temp,
            'Vc': crit_vol,
            'Tc': crit_temp,
            'dens': dens,
            'w':acent_fact,
            'P':press,
            'canonical_smiles': smiles
        }
        self.data_df = pd.DataFrame.from_dict(data_dict)
        data_descriptors_df = self._get_RDKit_descriptors()
        return 10**(self.model_pipeline.predict(data_descriptors_df))