#!/usr/bin/env python3
"""
Deployment Script for Tourism Package Prediction Project
"""

from huggingface_hub import HfApi, login
import os

#login(token=Tourism)

def deploy_to_huggingface_space():
    """Deploy application to HuggingFace Spaces"""
    print("Deploying to HuggingFace Spaces...")
    
    try:
        api = HfApi()
        space_id = "Anshika1211/Tourism_Package_Prediction"
        
        files_to_upload = [
            ("app.py", "app.py"),
            ("requirements.txt", "requirements.txt"),
            ("Dockerfile", "Dockerfile")
        ]
        
        print(f"Uploading files to space: {space_id}")
        
        for local_path, repo_path in files_to_upload:
            if os.path.exists(local_path):
                print(f"Uploading {local_path}...")
                api.upload_file(
                    path_or_fileobj=local_path,
                    path_in_repo=repo_path,
                    repo_id=space_id,
                    repo_type="space",
                    token=os.getenv('Tourism')
                )
                print(f"{local_path} uploaded successfully")
        
        print(f"\nDeployment completed!")
        print(f"App URL: https://huggingface.co/spaces/Anshika1211/Tourism_Package_Prediction")
        return True
        
    except Exception as e:
        print(f"Deployment error: {e}")
        return False

if __name__ == "__main__":
    deploy_to_huggingface_space()
