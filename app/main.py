from fastapi import FastAPI, Request 
from .endpoints import router 

def get_application():     
	app = FastAPI(root_path="/URL")     
	app.include_router(router)     
	return app

