# Import the module
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()
# Scraeping Instagram BIo
# Load a profil from an instageam hadnle
profile = instaloader.Profile.from_username(bot.context, 'instagram')
print(f"Username: {profile.username}")
print(f"User ID: {profile.userid}")
print(f"Number of Posts: {profile.mediacount}")
print(f"Followers: {profile.followers}")
print(f"Followees: {profile.followees}")
print(f"Bio: {profile.biography,profile.external_url}")

followees = [followee.username for followee in profile.get_followees()]

# Retrieve the usernames of all followers
followers = [follower.usename for follower in profile.get_followers()]

# Retrive the username of all followees
followees = [followee.username for followee in profile.get_followees()]
print(followers)


# Downloading Posts from Another Profile
# Load a new profile
profile = instaloader.Profile.from_username(bot.context, 'hi.vanee')

# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")