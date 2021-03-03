# flask_crud_api

Here's a CRUD API that simulates an Audio File Server.

This API is built with Flask and SQLAlchemy, it implents create, read, upload, and delete endpoints for an audio file as defined below:

Create API:
The request will have the following fields:
- audioFileType – mandatory, one of the 3 audio types possible
- audioFileMetadata – mandatory, dictionary, contains the metadata for one of the three audio files (song, podcast, audiobook)

Delete API:
- The route will be in the following format: "<audioFileType>/<audioFileID>"

Update API:
- The route be in the following format: “<audioFileType>/<audioFileID>”
- The request body will be the same as the upload

Get API:
- The route “<audioFileType>/<audioFileID>” will return the specific audio file
- The route “<audioFileType>” will return all the audio files of that type

Setup Instructions:
-Kindly use the 'requirements.txt' file to install all required python packages.
-Lines 6, 7, 8, & 9 of crudapi.py should be edited and appropriate database connection details filled
-The database connection string on Line 12 may also be replace for other supported SQL like PostgreSQL
-Four test have to provided to test each endpoint of the API, otherwise Postman App(https://www.postman.com/downloads/) may be a suitable alternative.
