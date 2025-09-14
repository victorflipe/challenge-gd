from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import traceback 
from .api.routes import article_routes, user_routes, tag_routes, comments_routes

app = FastAPI(title="TechBlog API", version="1.0")

@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "trace": traceback.format_exc().splitlines()  # detalhe do erro
            },
        )

app.include_router(article_routes.router)
app.include_router(user_routes.router)
app.include_router(tag_routes.router)
app.include_router(comments_routes.router)