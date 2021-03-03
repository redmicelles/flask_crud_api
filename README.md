# flask_crud_api

Here's a CRUD API that simulates an Audio File Server.

This API is built with Flask and SQLAlchemy, it implements create, read, upload, and delete endpoints for an audio file as defined below:

Create API:
The request will have the following fields:
- <strong>audioFileType<strong> – mandatory, one of the 3 audio types possible (song, podcast, audiobook)
- audioFileMetadata – mandatory, dictionary, contains the metadata for one of the three audio files (song, podcast, audiobook)
- Actual route: `http://localhost:5000/fileserver/create_file`

Delete API:
- The route will be in the following format: `<audioFileType>/<audioFileID>`
- Actual route: `http://localhost:5000/fileserver/delete_file/<audioFileType>/<audioFileID>`

Update API:
- The route be in the following format: `<audioFileType>/<audioFileID>`
- The request body will be the same as the upload
- Actual route: `http://localhost:5000/fileserver/update_file/<audioFileType>/<audioFileID>`

Get API:
- The route `<audioFileType>/<audioFileID>` will return the specific audio file
- The route `<audioFileType>` will return all the audio files of that type
- Actual route: `http://localhost:5000/fileserver/get_file/<audioFileType>/<audioFileID>`

Below are the request-body JSON-data format for each audio type:

Song file:
- name – (mandatory, string, cannot be larger than 100 characters)
- duration – (mandatory, integer, positive)
- uploaded_time – (mandatory, Datetime, cannot be in the past)

Podcast file:
- name – (mandatory, string, cannot be larger than 100 characters)
- duration – (mandatory, integer, positive)
- uploaded_time – (mandatory, Datetime, cannot be in the past)
- host – (mandatory, string, cannot be larger than 100 characters)
- Participants – (optional, list of strings, each string cannot be larger than 100 characters, maximum of 10 participants possible)
-
Audiobook file:
- title – (mandatory, string, cannot be larger than 100 characters)
- author of the title (mandatory, string, cannot be larger than 100 characters)
- narrator - (mandatory, string, cannot be larger than 100 characters)
- duration in number of seconds – (mandatory, integer, positive)
- uploaded_time – (mandatory, Datetime, cannot be in the past)

Setup Instructions:
- Kindly use the 'requirements.txt' file to install all required python packages.
- Lines 6, 7, 8, & 9 of crudapi.py should be edited and appropriate database connection details filled
- The database connection string on Line 12 may also be replace for other supported SQL like PostgreSQL
- Four tests have been provided, one for each endpoint of the API, otherwise Postman App(https://www.postman.com/downloads/) may be a suitable alternative for testing.
