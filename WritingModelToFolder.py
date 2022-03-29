with dataiku.Folder(FOLDER_ID).get_writer(MODEL_PATH_IN_FOLDER) as writer:
	writeable = pickle.dumps(MODEL)
	writer.write(writeable)
  
 ##Option 2 
  # Write recipe outputs #Problem here too
#change this part to something like 
Folder = dataiku.Folder("rlACbXYw")
path = Folder.get_path()

bytes_container = BytesIO()
model.save(bytes_container)
bytes_container.seek(0)

Folder.upload_stream("saved_model.model", bytes_container)        
        
Model_info = Model.get_info()
