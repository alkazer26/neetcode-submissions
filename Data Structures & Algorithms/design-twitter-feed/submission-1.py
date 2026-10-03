class Twitter:

    def __init__(self):
        self.follows = {} # followerId : {set of ther followeeIds}
        self.tweets = deque() # (userId, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        i = 0

        while i < len(self.tweets) and len(out) < 10:
            t_userId, tweetId = self.tweets[i]
            if t_userId == userId or (
                    userId in self.follows and t_userId in self.follows[userId]
                ):
                out.append(tweetId)

            i += 1
        
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
