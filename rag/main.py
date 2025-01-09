import uvicorn
from fastapi import FastAPI
from controllers import router


app = FastAPI(title="RAG System API")
app.include_router(router=router)


if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=8002)
