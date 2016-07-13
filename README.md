## celery-next-step

1. `sh setup.sh` to install required packages.
2. `sh start-worker.sh` to start celery workers.
3. `python3 tester.py` to test celery.

Note:
- These scripts was designed for running on new Ubuntu/Debian system (AWS instance for me), 
- also, assumed that `sudo` is available, so,
- comment out unnecessary lines in `setup.sh` is recommended.
- Using rabbitmq as broker by default.
- To use redis, run `setup-redis.sh` instead of `setup.sh`.
