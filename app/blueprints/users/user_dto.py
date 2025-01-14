from app.extensions import marshInstance
from marshmallow import validate
from marshmallow import ValidationError

def validate_password(passw):
    if len(passw) < 6 or len(passw) > 30:
        raise ValidationError("The 'password' must be at least 6 characters long.")


class UserDTO(marshInstance.Schema):
    name = marshInstance.Str(
        required=True,
        error_messages={"required": "The 'name' field is required."}
    )
    email = marshInstance.Email(
        required=True,
        error_messages={"required": "The 'email' field is required."}
    )
    password = marshInstance.Str(
        required=True,
        validate=validate_password, # aplicate a custom function
        error_messages={"required": "The 'password' field is required."}
    )
    # password = marshInstance.Str(
    # validate=lambda p: len(p) >= 6, it can be a lamda function
    # required=True,
    # validate=validate.Regexp( also a regex validation but only one at time
    #     regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$",
    #     error="Password must have at least one uppercase letter, one lowercase letter, one number, and be at least 6 characters long."
    #     )
    # )
    
    
class UpdateUserDto(marshInstance.Schema):
    name = marshInstance.Str(validate=validate.Length(min=1))  
    email = marshInstance.Email()  
    password = marshInstance.Str(validate=validate.Length(min=6)) 
    


user_dto = UserDTO()
update_user_dto = UpdateUserDto()
