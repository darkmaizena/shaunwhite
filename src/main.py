from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import logging
import uvicorn

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.post("/gatorservice/AuthenticationServiceSSL.svc")
async def authentication_service_ssl():
    return FileResponse("auth_response.xml")


@app.post("/gatorservice/ConfigService.svc")
async def config_service():
    return FileResponse("field_definitions.xml")


@app.post("/gatorservice/ContentService.svc")
async def content_service():
    return FileResponse("content_response.xml")


@app.post("/TransferService.svc")
async def transfer_service(request: Request):
    await request.body()
    return


@app.get("/MatchMakingConfig.aspx")
async def matchmaking_config():
    return FileResponse("MatchMakingConfig.aspx")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3074)
