## celery-next-step

A small demo of starting up Celery and testing the codes in the [documentation (section: Next Steps)](http://docs.celeryproject.org/en/latest/getting-started/next-steps.html)

1. `sh setup.sh` to install required packages.
2. `sh start-worker.sh` to start celery workers.
3. `python3 tester.py` to test celery.
4. There should be 4 lines of "x + y = z" printed on screen. Each demonstrated a way to use the "add" method defined in `proj/tasks.py`.
5. The first line get result from `a = tasks.add(1,2)`, which runs locally should always be printed.
6. The next three lines get results from codes below, respectively.
```
b = tasks.add.apply_async((3,4),); b.get()
c = tasks.add.delay(5,6); c.get()
d = tasks.add.s(7,8); d()
```

Note:
- These scripts was designed for running on new Ubuntu/Debian system (AWS instance for me),
- also, assumed that `sudo` is available, so,
- comment out unnecessary lines in `setup.sh` is recommended.
- Using rabbitmq as broker by default.
- To use redis, run `setup-redis.sh` instead of `setup.sh`.
