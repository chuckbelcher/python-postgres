# importing fuct tools to maintain the function name when using secure_function
import functools

user = {"username": "Jose", "access_level": "guest"}


def make_secure(func):
    # add wraps function to keep original function name
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


@make_secure
def get_password(panel):
    if panel == "admin":
        return 1234
    elif panel == "billing":
        return "super_secret_billing_password"


print(get_password("billing"))
