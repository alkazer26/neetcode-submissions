class Twitter:
    def __init__(self):
        self.follows = {}  # followerId : {set of ther followeeIds}

        # userId : [list of their tweets], where tweet is (cnt, tweetId)
        self.tweets = {}
        self.cnt = 0  # lower/negative = more recent

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].appendleft((self.cnt, tweetId))
        else:
            self.tweets[userId] = deque([(self.cnt, tweetId)])

        self.cnt -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # combine all the potential tweets associated with a user
        heap = []

        if userId not in self.follows:
            self.follows[userId] = set()
        
        self.follows[userId].add(userId)

        for followee in self.follows[userId]:
            if followee in self.tweets:
                for i in range(min(10, len(self.tweets[followee]))):
                    heap.append(self.tweets[followee][i])

        heapq.heapify(heap)
        out = []

        while len(out) < 10 and heap:
            _, tweetId = heapq.heappop(heap)
            out.append(tweetId)

        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
