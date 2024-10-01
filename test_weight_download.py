from deepface.commons.weight_utils import download_weights_if_necessary

# Define the file name and the GCP URL for the weights
file_name = "facenet_finetuned_firstrun_v1.keras"
source_url = "https://storage.googleapis.com/photo-search-bucket/Custom%20weights%20vivek/facenet_finetuned_firstrun_v1.keras"

# Trigger the download process
downloaded_file = download_weights_if_necessary(file_name, source_url)

# Print the path of the downloaded file for confirmation
print(f"Weights downloaded to: {downloaded_file}")
