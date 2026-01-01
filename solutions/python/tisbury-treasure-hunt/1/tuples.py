"""Functions to help Azara and Rui locate pirate treasure."""

def get_coordinate(record):
    return record[-1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    return tuple(get_coordinate(azara_record)) == rui_record[-2]

def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"
    
def clean_up(combined_record_group):
    return "".join([f"{(record[0], record[2], record[3], record[4])}\n" for record in combined_record_group])



    