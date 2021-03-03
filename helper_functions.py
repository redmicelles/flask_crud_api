from datetime import date, datetime

def check_file_type(file_type):
    file_types = {'Song', 'Podcast', 'Audiobook'} #Allowed file types
    if file_type == None:
        return False
    return (file_type.capitalize() in file_types)

def check_string(fieldname):
    if fieldname == None:
        return False
    elif len(fieldname) > 100:
        return False
    return True

def check_duration(duration):
    if duration == None:
        return False
    elif not duration.isdigit():
        return False
    return True

def check_date(dt):
    if dt == None:#dt format 2018-11-30 09:15:32
        return False
    return datetime.now() <= datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")

def validate_song(data_):
    return not all(
                (
                    check_string(data_['name']), 
                    check_duration(data_['duration']),
                    check_date(data_['uploaded_time'])
                )
            )
    
def validate_podcast(data_):
    return not all(
                (
                    check_string(data_['name']), 
                    check_duration(data_['duration']),
                    check_date(data_['uploaded_time']),
                    check_string(data_['host']),
                    check_string(data_['participants']),
                )
            )
    
def validate_audiobook(data_):
    return not all(
                (
                    check_string(data_['title']), 
                    check_string(data_['author']),
                    check_string(data_['narrator']),
                    check_duration(data_['duration']),
                    check_date(data_['uploaded_time'])
                )
            )

    

