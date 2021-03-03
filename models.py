from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Song(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    time_uploaded = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, name, duration, time_uploaded):
        self.name = name
        self.duration = duration
        self.time_uploaded = time_uploaded
    
    
class Podcast(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    time_uploaded = db.Column(db.DateTime, nullable=False)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.String(118), nullable=True)
    
    def __init__(self, name, duration, time_uploaded, host, participants):
        self.name = name
        self.duration = duration
        self.time_uploaded = time_uploaded
        self.host = host
        self.participants = participants
    
class Audiobook(db.Model):
    id = db.Column('id', db.Integer, primary_key = True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    time_uploaded = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, title, author, narrator, duration, time_uploaded):
        self.title = title
        self.author = author
        self.narrator = narrator
        self.duration = duration
        self.time_uploaded = time_uploaded

   
def insert_file(audioFileType, data):
    file_data = ''
    data_ = data['audioFileMetadata']
    if audioFileType.lower() == 'song':
        file_data = Song(data_['name'], data_['duration'], data_['uploaded_time'])
        
    elif audioFileType.lower() == 'podcast':
        file_data = Podcast(data_['name'], data_['duration'], data_['uploaded_time'],
                            data_['host'], data_['participants'])
         
    elif audioFileType.lower() == 'audiobook':
        file_data = Audiobook(data_['title'], data_['author'], data_['narrator'],
                              data_['duration'], data_['uploaded_time'])
        
    db.session.add(file_data)
    db.session.commit()
    
#delete audio file from file type by file id  
def delete_audiofile(audioFileType, file_id):
    eval(f'{audioFileType.capitalize()}.query.filter_by(id=file_id).delete()')
    

# update audio files function, using if and elif to switch control to the requested file type   
def update_audiofile(audioFileType, file_id, data):
    update_data = ''
    data_ = data['audioFileMetadata']
    if audioFileType.lower() == 'song':
        update_data = Song.query.filter_by(id=file_id).update(dict(name=data_['name'],
                                                                    duration=data_['duration'],
                                                                    time_uploaded=data_['uploaded_time'])
                                                            )
    elif audioFileType.lower() == 'podcast':
        update_data = Podcast.query.filter_by(id=file_id).update(dict(name=data_['name'],
                                                                duration=data_['duration'],
                                                                time_uploaded=data_['uploaded_time'],
                                                                host=data_['host'],
                                                                participants=data_['participants']
                                                                )
                                                        )    
       
    elif audioFileType.lower() == 'audiobook':
        update_data = Audiobook.query.filter_by(id=file_id).update(dict(title=data_['title'],
                                                                        author=data_['author'],
                                                                        narrator=data_['narrator'],
                                                                        duration=data_['duration'],
                                                                        time_uploaded=data_['uploaded_time'],
                                                                        )
                                                                )    
    db.session.commit()

#Query database for files    
def get_audiofile(audioFileType, file_id):
    if file_id == None: #if file id is not specified, return all rows of audio type
        return eval(f'{audioFileType.capitalize()}.query.filter().all()')
    return eval(f'{audioFileType.capitalize()}.query.filter_by(id=file_id)') #fetch single row in audio type by id
     