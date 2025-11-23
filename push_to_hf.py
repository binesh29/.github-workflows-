from huggingface_hub import HfApi
import os

api = HfApi()
repo_id = "binesh-b/GL_Project_Tourism_Backend"

api.upload_folder(
    folder_path="tourism_project/artifacts",
    repo_id=repo_id,
    repo_type="space",
    token=os.environ["HF_TOKEN"]
)

print("Updated model pushed to HuggingFace 🚀")
