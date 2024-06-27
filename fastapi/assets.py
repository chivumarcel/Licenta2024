from fastapi import FastAPI

app = FastAPI()

ASSETS = [
    {'title':'WF-RAC-Connection_manual_with_Alexa.pdf', 'author':'Mitsubishi', 'cathegory':'connection-manual',
    'url':'https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/'},
    {'title':'WF-RAC-Connection_manual_with_Google.pdf', 'author':'Mitsubishi', 'cathegory':'connection-manual',
    'url':'https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/'},
    {'title': 'WF-RAC-Databook.pdf', 'author': 'Mitsubishi', 'cathegory': 'data book',
     'url': 'https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/'},
    {'title': 'WF-RAC-Databook.pdf', 'author': 'Mitsubishi', 'cathegory': 'data book',
     'url': 'https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/'},
    {'title': 'WF-RAC-Setup_Quick_Guide_to_the_Remote_Control_System_Configuration_for_RAC.pdf', 'author': 'Mitsubishi', 'cathegory': 'quick-guide',
     'url': 'https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/'},
    {'title': 'WF-RAC-Smart_M-Air_AppManual-English(EEA,UK).pdf', 'author': 'Mitsubishi', 'cathegory': 'operation-manual',
     'url': 'https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/'},
    {'title': 'WF-RAC-Smart_m_air_FAQ_english.pdf', 'author': 'Mitsubishi', 'cathegory': 'FAQ',
     'url': 'https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/'},
    {'title': 'WF-RAC-Wireless LAN connection manual_EN_Web ZTL.pdf', 'author': 'Mitsubishi', 'cathegory': 'WiFi-connection',
     'url': 'https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/'},
    {'title': 'WF_RAC-Wireless LAN connection manual_EN_Web ZSX.pdf', 'author': 'Mitsubishi', 'cathegory': 'WiFi-connection',
     'url': 'https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/'},
    {'title': 'WF_RAC-INSTALLATION MANUAL_english.pdf', 'author': 'Mitsubishi', 'cathegory': 'installation-manual',
     'url': 'https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/'}
]

@app.get("/assets") #URL ca parametru static
async def read_all_assets():
    return ASSETS

# @app.get('/assets/{dynamic_param}') #URL ca parametru dinamic
# async def read_all_assets(dynamic_param: str):
#     return {'dynamic_param': dynamic_param}

@app.get('/assets/{asset_title}')
async def read_asset(asset_title: str):
    for asset in ASSETS:
        if asset.get('title').casefold() == asset_title.casefold():
            return asset

@app.get('/assets/{asset_title}')
async def read_asset(asset_title: str, categpory:str):
    assets_to_return = []
    for asset in ASSETS:
        if asset.get('title').casefold() == asset_title.casefold() and asset.get('category').casefold() == categpory.casefold():
            assets_to_return.append(asset)
    return assets_to_return

@app.get('/assets/')
async def read_category_by_query(category: str):
    assets_to_return = []
    for asset in ASSETS:
        if asset.get('category').casefold() == category.casefold():
            assets_to_return.append(asset)
    return assets_to_return

# @app.get("/api-endpoint")
# async def first_api():
#     return {"Message": "Connected!"}



