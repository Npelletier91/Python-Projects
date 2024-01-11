import os
from google.cloud import storage
from google.cloud import aiplatform

PROJECT_ID = "infra-rhino-410923"
REGION = "us-central1"

BUCKET_NAME = "new_bucket_345366"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Nicol\\Documents\\infra-rhino-410923-34b1cd6ada2b.json"

def create_bucket(bucket_name):
    """
    Create a Cloud Storage bucket with the given name.
    """
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print("Bucket Created:", bucket.name)
    
def upload_dataset(bucket_name, dataset_path):
    """
    Uploads a dataset file to the specified Cloud Storage bucket.
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(os.path.basename(dataset_path))
    blob.upload_from_filename(dataset_path)
    print("Dataset file uploaded to Cloud Storage")

def create_tabular_dataset(bucket_name, dataset_path):
    """
    Create a Tabular Dataset in Vertex AI using the specified bucket and dataset file.
    """
    aiplatform.init(project=PROJECT_ID, location=REGION)
    gcs_source_uri = f"gs://{bucket_name}/{os.path.basename(dataset_path)}"
    dataset = aiplatform.TabularDataset.create(display_name="my-dataset", gcs_source=gcs_source_uri)
    print("Tabular Dataset created", dataset.display_name)

def analyze_dataset(bucket_name, dataset_path):
    dataset = aiplatform.TabularDataset(
        project=PROJECT_ID,
        location=REGION,
        display_name="mydata_set",
        gcs_source=f"gs://{bucket_name}/{os.path.basename(dataset_path)}"
    )
    analysis = dataset.analyze()
    print("Dataset analysis results:")
    print(analysis)

def main():
    """
    Main function that orchestrates the steps ot create the bucket, upload the dataset, and create the Tabular Dataset.
    """
    create_bucket(BUCKET_NAME)
    upload_dataset(BUCKET_NAME, r"C:\\Users\\Nicol\\Documents\\Python Practice\\image_dataset.csv")
    create_tabular_dataset(BUCKET_NAME, r"C:\\Users\\Nicol\Documents\\Python Practice\\image_dataset.csv")
    analyze_dataset(BUCKET_NAME, r"C:\\Users\\Nicol\Documents\\Python Practice\\image_dataset.csv")
    
if __name__ == "__main__":
    main()