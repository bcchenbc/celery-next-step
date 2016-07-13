# [optional] start a flower instance for monitoring celery workers
celery -A proj flower &
# start 2 workers 
celery -A proj worker -n celery01 &
celery -A proj worker -n celery02 &

