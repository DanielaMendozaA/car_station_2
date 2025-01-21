import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI') 
    @classmethod
    def validate_enviroment_variables(clase):
        required_variables = ['MONGO_URI']
        missing_variables = [var for var in required_variables if not getattr(clase, var)]
        
        if(missing_variables):
            raise ValueError(f"The following variables are not defined: {', '.join(missing_variables)}")

Config.validate_enviroment_variables()