
class Operate:

    def __init__(self):
        pass
    
    def search_serial_from_coord(self, df, target_serial_number):
        '''
        シリアル番号から該当する座標情報を持つ原子をサーチ
        '''
        query1 = "serial_number == @target_serial_number"
        df = df.query(query1)
        return [df.iloc[0]['x_coord'], df.iloc[0]['y_coord'], df.iloc[0]['z_coord']]
        

    def search_coord_from_model(self, df, target_coord):
        '''
        座標情報から該当するMODELをサーチ
        '''
        query1 = "x_coord == @target_coord[0] and y_coord == @target_coord[1] and z_coord == @target_coord[2]"
        target_atom_df = df.query(query1)
        
        target_model_id = target_atom_df.iloc[0]['model_id']
        query2 = 'model_id == @target_model_id'
        model_df = df.query(query2)
        
        return model_df
    
    def output_pdb(self, model_df):
        '''
        検索したMODELから分子モデリング用PDBの出力
        '''
        with open('result.pdb', encoding='utf-8', mode='a') as f:
            f.write('REMARK XXXX')
            f.write('\n')
            for i in range(len(model_df)):
                f.write('ATOM')
                f.write('  ')
                f.write(str(model_df.iloc[i]['model_id']))
                f.write('  ')
                f.write(str(model_df.iloc[0]['atom']))
                f.write('  ')
                f.write(str(model_df.iloc[0]['x_coord']))
                f.write('  ')
                f.write(str(model_df.iloc[0]['y_coord']))
                f.write('  ')
                f.write(str(model_df.iloc[0]['z_coord']))
                f.write('\n')
            f.write('TER')
            f.write('\n')