# Instagram System Design

## Requirements
- Upload images from a mobile client (Cloud?)
- User follow other users
- Generate feed of images (Expected latency?)
- Scale: 10 million users 

10 million:
- Monthly 
- 2 Photos/month
- 5MB (including metadata), boils down to 100 TB monthly 

- Data is relational, users own photos. Being able to quickly get all photos for a single user is 
inherently relational
User:
| 

Photo:

