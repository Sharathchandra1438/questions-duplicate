# Duplicate Question Detector (Streamlit)

This folder contains the Streamlit app to check whether two questions are duplicates.

Quick run (local):

```bash
cd streamlit-app
python -m pip install -r requirements.txt
streamlit run streamlit-app/app.py
```

Deployment (Streamlit Community Cloud):

1. Push the repository to GitHub (public or private).
2. On https://share.streamlit.io click "New app" and select your repo and branch.
3. Set the main file path to `streamlit-app/app.py` and deploy.

Notes
- The app gracefully falls back to a heuristic (TF-IDF + fuzzy features) when `model.pkl` or `cv.pkl` are missing.

Contact
- Ask me to (a) copy `model.pkl`/`cv.pkl` into this folder, (b) add download code for hosted artifacts, or (c) push the repo to GitHub and I can help finalize Streamlit deploy steps.
