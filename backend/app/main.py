from fastapi import FastAPI

app = FastAPI(title='Blog to Podcast Agent')

@app.get('/')
def health_check():
  return {'status': 'ok'}