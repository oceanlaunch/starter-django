# Django starter for OceanLaunch

A small Django site with a visit counter, ready to deploy on [OceanLaunch](https://oceanlaunch.cloud) with a managed
PostgreSQL database.

## Deploy it

In your OceanLaunch workspace, open **Templates** and choose **Django**. OceanLaunch:

- creates a PostgreSQL database and connects it (`DATABASE_URL`, read by `dj-database-url`);
- sets a random `SECRET_KEY` and `DJANGO_DEBUG=false`;
- installs `requirements.txt` and runs `python manage.py collectstatic --noinput` while building;
- starts it with `sh start.sh`: migrations, then gunicorn on the app's port.

Static files are served by WhiteNoise. The health check is `/health/`.

## Settings from the environment

| Variable | What it does |
|---|---|
| `SECRET_KEY` | Django's secret key (set for you) |
| `DJANGO_DEBUG` | `true` shows debug pages; keep it `false` when live |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated host names; `*` by default |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Extra trusted origins for forms, like `https://www.example.com` |
| `DATABASE_URL` | The database (set when one is connected); SQLite locally |

## An admin user

Open the app's **Console** tab and run:

```bash
DJANGO_SUPERUSER_PASSWORD='choose-a-long-password' python manage.py createsuperuser --noinput --username admin --email you@example.com
```

Then sign in at `/admin/`.

## Make it yours

Use **Make it yours** on the app's page (or GitHub's **Use this template**) to get your own copy, then push to it:
every push to `main` deploys again.

## Locally

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
