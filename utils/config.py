import os

LOGIN_URL = os.getenv(
    "HUDL_LOGIN_URL",
    "https://identity.hudl.com/u/login/identifier?state=hKFo2SAyNEk1dTU0UkkwclVFcDJVVFI3N2hJUmlVcHFiMTBfVKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIENjRXpENWJHUWVBekg0TjRjUFRQWUV3WG9nSERBTnE3o2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU"
)
PASSWORD_URL = os.getenv(
    "HUDL_PASSWORD_URL",
    "https://identity.hudl.com/u/login/password?state=hKFo2SAyNEk1dTU0UkkwclVFcDJVVFI3N2hJUmlVcHFiMTBfVKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIENjRXpENWJHUWVBekg0TjRjUFRQWUV3WG9nSERBTnE3o2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU"
)
