class Twitter:

    def __init__(self):
        self.feed = deque()
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        return [tweet for user, tweet in self.feed if user == userId or user in self.following[userId]][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
         self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)