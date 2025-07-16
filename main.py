import uvicorn
from fastapi.exceptions import RequestValidationError
from fastapi import Request, status
from fastapi.responses import JSONResponse
from datetime import datetime
from app import get_application
import logging

app = get_application()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	logging.error(f"{request}: {exc_str} \n##  Error at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
	content = {'status_code': 422, 'message': exc_str, 'data': None}
	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
