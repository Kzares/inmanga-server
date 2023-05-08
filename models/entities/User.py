class User():

    def __init__(self, id, username, password, hidden, saved, liked ) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.hidden = hidden
        self.saved = saved
        self.liked = liked
    def to_JSON(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "hidden": self.hidden,
            "saved": self.saved,
            "liked": self.liked
        }