from google.cloud import firestore
from google.oauth2 import service_account
from google import genai

SERVICE_ACCOUNT_FILE = "google key/tenxds-agents-idp-b7d6f705f5c1.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

client = genai.Client(
    credentials=credentials,
    vertexai=True,
    project=credentials.project_id,
    location="us-central1"
)

db = firestore.Client(
    project=credentials.project_id,
    credentials=credentials,
    database="nimesh-data"
)