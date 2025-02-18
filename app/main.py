from fastapi import FastAPI
from app.routers import categories, products, auth, prava


app = FastAPI()
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(prava.router)




