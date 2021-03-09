# TikTok System Design
- Identify to focus on (Backend) or Infra or Frontend

## Assumptions, Functional Requirements:
- Video comes in from API
- Videos are timeboxed, max 1 minute long
- Text on videos
- Aggregate videos, For You page

## Non functional requirements:
- Has to be a highly available system, 99.9%, can balance budget if no need for highly available
- Scale: 1M DAU

## Design
- Object containing video url, video stored on S3 Cloud bucket
- Store video table in a relational DB, SQL is more structured, easier joins
- Want to preload videos, even cache it on the frontend a small amount like 3
- Precache service to store list of next videos, can be done on a schedule or after every login
  - This should be done from a read only replica of the DB
  - Don't want users to wait when they open up the app for backend to give suggestions
  - Also scales better, when a million users come online at once
  - Very read heavy
- A new table for user activities
  - list of people user is following, foreign key
  - video likes is another relationship with uuid

- What if you 10x the traffic?
  - Have regional datacenters, put API endpoints behind a CDN, content delivery network
    - CDN, if a celebrity sends out a video, it caches the video for next users to pull directly
    - Load Balancer
  - Bottlenecks in DB, one main write database
    - Some sort of database sharding, for example regional sharding
  - Bottlenecks in uploading video, spin up more instances
  - Cache is pretty scalable

- Do you have any extra questions? I would love to get in more about the X service (Precaching)
because it might need its own db structure.
  - It's always interesting designing something you've never used
