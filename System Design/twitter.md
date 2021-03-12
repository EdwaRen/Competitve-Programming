# Twitter System Design

## Features
- Tweet, timeline (Home, User, Search), Trends
- Handle celebrities sending out a tweet to millions of followers
- Read Heavy
- Ok to have eventual consistency
- Storage

## Design
- Horizontal scaling,
- We should use Redis and DB
- User table, tweet table, follower table
- Can store tweets and followers like
  <USERID>-Tweets: [1, 2, 3, ...]

## Timeline
- Timeline, we have to preprocess tweets as they come in. so 1 cache access to get timeline rather
  than going through all followers and all tweets
    - Fanout: the number of gates driven by the output of a single logic gate.
    - For every tweet write, we fanout the timelines of each follower to include the tweet
    - However, it can takes minutes to update celebrity tweets
      - Special case to handle celebrities, go through all celebrities and get
      their tweets individually (cache celebrity tweets to make this even faster)
    - To optimize even more, we can stop calculating timeline for inactive users

## Tweets
  - Find trending Tweets
    - Filter for hashtags
    - Count, Rank, map to geolocation
    - Done via streaming (Kafka)

## Searching
