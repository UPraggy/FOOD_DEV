import CRUD_data as cd 
class Order_functions: 
    def create(file_path_origin, file_path_destination):
        cd.insert_data(file_path_origin, file_path_destination)

    def select(file_path_origin, field_src):
        cd.select_data(file_path_origin, field_src)

    def update(file_path_origin, file_path_destination, field_src):
        cd.update_data(file_path_origin, file_path_destination, field_src)

    def delete(file_path_origin, file_path_destination, field_src):
        cd.delete_data(file_path_origin, file_path_destination, field_src)