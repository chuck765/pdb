import pdb_data.data_model as data_model
import pdb_data.operate as pdb_ope

# インスタンス化
pdb_data_model = data_model.DataModel()
pdb_ope = pdb_ope.Operate()

# PDBデータを保持したデータフレームを取得
sim_df = pdb_data_model.get_data_frame('./pdb_data/sample.pdb')
print(sim_df)

serial_number = 1
target_coord = pdb_ope.search_serial_from_coord(sim_df, serial_number)
model_df = pdb_ope.search_coord_from_model(sim_df, target_coord)
pdb_ope.output_pdb(model_df)