# AI Tutor MVP (in progress)
Personalised AI tutor that lets companies onboard new hires from their own training videos.

## Working now
- Firestore security rules enforcing per-company data isolation
- Python backend using the Firebase Admin SDK (auth, write, query)
- Test script: `test_firestore.py`

## Planned
- Retrieval-Augmented Generation (RAG) over training video transcripts

## Run the tests
1. Install: `pip install firebase-admin`
2. Add your own service account key (never commit it)
3. `python test_firestore.py`
