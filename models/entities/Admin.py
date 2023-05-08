class Admin():

    def __init__(self, id, username, password ) -> None:
        self.id = id
        self.username = username
        self.password = password
    def to_JSON(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password
        }