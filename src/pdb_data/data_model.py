# 標準ライブラリ
from functools import singledispatch
import os
import pandas as pd
from typing import List
import warnings

# サードパーティ製
from Bio.PDB import *

# Biopythonの警告ログを非表示
warnings.filterwarnings('ignore')

class DataModel:
    
    def __init__(self):
        pass
    
    def get_data_frame(self, pdb_file):
        '''
        PDBデータを保持したデータフレームを取得
        '''
        structure = PDBParser().get_structure('X', pdb_file)
        df_data = {}
        serial_number_list = []
        model_id_list = []
        atom_list = []
        x_coord_list, y_coord_list, z_coord_list = [], [], []
        bfactor_list = []
        for model in structure.get_list():
            for chain in model.get_list():
                for residue in chain.get_list():
                    for atom in residue.get_list():
                        model_id_list.append(model.id)
                        serial_number_list.append(atom.get_serial_number())
                        atom_list.append(atom)
                        x_coord_list.append(atom.get_coord()[0])
                        y_coord_list.append(atom.get_coord()[1])
                        z_coord_list.append(atom.get_coord()[2])
                        bfactor_list.append(atom.get_bfactor())
                        
        df_data['model_id'] = model_id_list
        df_data['serial_number'] = serial_number_list
        df_data['atom'] = atom_list
        df_data['x_coord'] = x_coord_list
        df_data['y_coord'] = y_coord_list
        df_data['z_coord'] = z_coord_list
        df_data['bfactor'] = bfactor_list
        
        return pd.DataFrame(df_data)
