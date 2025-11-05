from typing import Dict, Set, List
from collections import defaultdict

class Twitter:
    # m = users, n = tweets, k = feed-size

    def __init__(self):
        self.follows: Dict[int, Set[int]] = defaultdict(set) # [userId] -> {userId}
        self.tweets: Dict[int, List[int]] = defaultdict(list) # [userId] -> tweetId

        self.time_id = 0
        self.tweet_to_time: Dict[int, int] = {}

        # only contains entries for most recent `time_id`s
        # since dictionaries are sorted in python, this is our doubly linked list
        # (we use `tweets` and `tweet_to_time` to get a node by userId)
        self.recentmost_tweets: Dict[int, int] = {} # [time_id] -> userId

    # O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        this_time_id = self.time_id
        self.tweet_to_time[tweetId] = this_time_id
        self.time_id += 1

        users_tweets = self.tweets[userId]
        if users_tweets:
            users_recentmost_tweet_id = users_tweets[-1]
            users_recentmost_time_id = self.tweet_to_time[users_recentmost_tweet_id]
            del self.recentmost_tweets[users_recentmost_time_id]
        self.recentmost_tweets[this_time_id] = userId

        self.tweets[userId].append(tweetId)

    # O(m + k^2 * lg(k))
    # (filtering a linked list of size m, then sorting an array of size k^2)
    def getNewsFeed(self, userId: int) -> List[int]:
        k = 10
        followed_users_sorted = [uid for uid in self.recentmost_tweets.values() if uid == userId or (uid in self.follows[userId])]
        k2_tweets = [self.tweets[uid][-k:] for uid in followed_users_sorted[:k]] # k recentmost tweets of each of the k recentmost tweeting followed users
        k2_tweets = [x for xs in k2_tweets for x in xs] # flatten
        return list(reversed(sorted(k2_tweets, key=lambda id: self.tweet_to_time[id])[-k:]))

    # insert in tree of size m = O(log(m))
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId] |= {followeeId}

    # insert in tree of size m = O(log(m))
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId] -= {followeeId}