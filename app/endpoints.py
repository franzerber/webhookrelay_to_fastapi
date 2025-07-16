

from fastapi import APIRouter, Request, Header, status 
from fastapi.responses import JSONResponse 
from datetime import datetime 
from pydantic import BaseModel
from .telegram.telegram_main import send_telegram_message

WHITELISTED_IPS = []
router = APIRouter()

class InputData(BaseModel):
    data_dict: dict


@router.get("/")
async def root(real_ip: str = Header(None, alias='X-Real-IP'), jobtype: str = "unknown", message: str = "unknown"):
    print(f"INFO:     NEW JOB GET   ###   - - -   jobtype: {jobtype}   msg: {message}     ###   - - -    ###   - - -    ###")
    result_msg = {"statusCode": "ERROR", 
            "statusMessage": f"webhookrelay_to_fastapi,  jobtype: {jobtype}",
            "EndTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    if jobtype != "unknown":
        result_msg = send_telegram_message(jobtype, message)
    return result_msg

@router.post("/")
async def post_config(data_dict: InputData, request: Request, real_ip: str = Header(None, alias='X-Real-IP')):
    """
    IP Source check API Security !!!
    """
    print(f"INFO:     NEW JOB POST   ###   - - -   ###   - - -    ###   - - -    ###")
    msg = {"statusCode": "OK", 
            "statusMessage": "webhookrelay_to_fastapi, ",
            "EndTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """
    start
    """
    print(data_dict)
    return f"DATA: {data_dict} ---\n"
