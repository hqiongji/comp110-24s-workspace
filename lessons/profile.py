"""dddd."""

# Definition Part
class Profile:
    user_name: str
    private: bool

    def __init__(self, user_name_input: str):
        """Create a new Profile object."""
        self.user_name = user_name_input
        self.private = True

    def tweet(self, msg: str) -> None: 
        """If profile is public, print msg."""
        if self.private is False:
            print(msg)

#Instantiation
user1: Profile = Profile("110_rulez") #calls __init__
user1.private = False 
user1.tweet("Oop is cool.")
