from fastapi import Body, FastAPI

app = FastAPI()

ASSETS = [
    {"title":"WF-RAC-Connection_manual_with_Alexa.pdf", "author":"Mitsubishi", "category":"connection-manual",
    "url":"https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"},
    {"title":"WF-RAC-Connection_manual_with_Google.pdf", "author":"Mitsubishi", "category":"connection-manual",
    "url":"https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"},
    {"title": "WF-RAC-Databook.pdf", "author": "Mitsubishi", "category": "data book",
     "url": "https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"},
    {"title": "WF-RAC-Databook.pdf", "author": "Mitsubishi", "category": "data book",
     "url": "https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"},
    {"title": "WF-RAC-Setup_Quick_Guide_to_the_Remote_Control_System_Configuration_for_RAC.pdf", "author": "Mitsubishi", "category": "quick-guide",
     "url": "https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"},
    {"title": "WF-RAC-Smart_M-Air_AppManual-English(EEA,UK).pdf", "author": "Mitsubishi", "category": "operation-manual",
     "url": "https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"},
    {"title": "WF-RAC-Smart_m_air_FAQ_english.pdf", "author": "Mitsubishi", "category": "FAQ",
     "url": "https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"},
    {"title": "WF-RAC-Wireless LAN connection manual_EN_Web ZTL.pdf", "author": "Mitsubishi", "category": "WiFi-connection",
     "url": "https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"},
    {"title": "WF_RAC-Wireless LAN connection manual_EN_Web ZSX.pdf", "author": "Mitsubishi", "category": "WiFi-connection",
     "url": "https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"},
    {"title": "WF_RAC-INSTALLATION MANUAL_english.pdf", "author": "Mitsubishi2", "category": "installation-manual",
     "url": "https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"},
    {
        "title": "WF_RAC-INSTALLATION-MANUAL_english-v2test.pdf",
        "author": "Mitsubishi",
        "category": "manual",
        "url": "https://github.com/chivumarcel/Licenta2024/blob/main/fastapi/assets/"
    }
]

# @app.get("/api-endpoint")
# async def first_api():
#     return {"Message": "Connected!"}

# modalitate de filtrare date in functie de URL; ATENTIE ORDINEA DE MAI JOS CONTEAZA!!! // de la granulatie mica la mare
@app.get("/assets") #URL ca parametru static
async def read_all_assets():
    return ASSETS

# @app.get("/assets/{dynamic_param}") #URL ca parametru dinamic
# async def read_all_assets(dynamic_param: str):
#     return {"dynamic_param": dynamic_param}

@app.get("/assets/{asset_title}")
async def read_asset(asset_title: str):
    for asset in ASSETS:
        if asset.get("title").casefold() == asset_title.casefold():
            return asset

# @app.get("/assets/byauthor/{asset_author}")
# async def read_assets_by_author_path(asset_author: str):
#     assets_to_return = []
#     for asset in ASSETS:
#         if asset.get("author").casefold() == asset_author.casefold():
#             assets_to_return.append(asset)
#             return assets_to_return

@app.get("/assets/byauthor/")
async def read_assets_by_author_path(asset_author: str):
    assets_to_return = []
    for asset in ASSETS:
        if asset.get("author").casefold() == asset_author.casefold():
            assets_to_return.append(asset)
            return assets_to_return

@app.get("/assets/{asset_title}")
async def read_asset(asset_title: str, category:str):
    assets_to_return = []
    for asset in ASSETS:
        if asset.get("title").casefold() == asset_title.casefold() and asset.get("category").casefold() == category.casefold():
            assets_to_return.append(asset)
    return assets_to_return

@app.get("/assets/")
async def read_category_by_query(category: str):
    assets_to_return = []
    for asset in ASSETS:
        if asset.get("category").casefold() == category.casefold():
            assets_to_return.append(asset)
    return assets_to_return

@app.get("/assets/{author}/")
async def read_author_category_by_query(author: str, category: str):
    assets_to_return = []
    for asset in ASSETS:
        if (asset.get("author").casefold() == author.casefold() and asset.get("category").casefold() == category.casefold()):
            assets_to_return.append(asset)
    return assets_to_return

#GET - nu are body, POST are body
@app.post("/assets/create_asset")
async def create_asset(new_asset=Body()):
    ASSETS.append(new_asset)

@app.put("/assets/update_asset")
async def update_asset(updated_asset=Body()):
    for i in range(len(ASSETS)):
        if ASSETS[i].get("title").casefold() == updated_asset.get("title").casefold():
            ASSETS[i] = updated_asset


@app.delete("assets/delete_asset/{asset_title}")
async def delete_asset(asset_title: str):
    for i in range(len(ASSETS)):
        if ASSETS[i].get("title").casefold() == asset_title.casefold():
            ASSETS.pop(i)
            break
