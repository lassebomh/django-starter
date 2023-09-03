#!/bin/sh

celery -A mysite.celery worker -l info