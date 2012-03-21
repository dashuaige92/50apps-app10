worker: python market/manage.py celeryd -E -B --loglevel=INFO
web: python hellodjango/manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3
