from fastapi import FastAPI

app = FastAPI()

@app.get("/api-endpoint")
async def first_api():
    return {"Message": "Connected!"}

@app.get("/assets")
async def read_all_assets():
    return ASSETS

ASSETS = {
    'title':'WF_RAC-INSTALLATION MANUAL_english.pdf', 'author':'Mitsubishi', 'cathegory':'installation manual',
    'url':'https://github.com/Mitsubishi/WF_RAC-INSTALLATION'},

}