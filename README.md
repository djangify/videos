# 📹 Djangify Videos

A lightweight, self-hosted video tutorial platform built with Django. It powers [videos.djangify.com](https://videos.djangify.com) — a short-form tutorial library for users of the [Djangify eCommerce Builder](https://github.com/djangify/ebuilder).

---

## What It Does

Djangify Videos is a clean, no-frills video hosting site. Videos are stored on the server and served directly from a `/library/` path. The site organises tutorials into categories with a simple sidebar navigation, and each video has its own detail page with a related videos section.

It is intentionally small and focused — no JavaScript framework, no external CDN dependencies, no unnecessary complexity.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 5.2 |
| Admin Theme | [Adminita](https://github.com/djangify/adminita) |
| Static Files | WhiteNoise |
| Configuration | django-environ |
| Database | SQLite |
| Deployment | Self-hosted VPS |

---

## Adminita

The Django admin is themed with **[Adminita](https://github.com/djangify/adminita)** — a modern, open-source Django admin theme built with Tailwind CSS v4. It replaces Django's default admin with a clean, responsive interface that includes dark mode support.

Adminita is a standalone package available on [PyPI](https://pypi.org/project/adminita/) and maintained separately as its own open-source project. It can be dropped into any Django project.

```python
INSTALLED_APPS = [
    "adminita",  # Must be before django.contrib.admin
    "django.contrib.admin",
    ...
]
```

---

## App Structure

The core of the project lives in a single Django app called `tube`.

```
tube/
├── models.py       # Category and Video models
├── views.py        # List, category, and detail views
├── urls.py         # URL routing
└── admin.py        # Admin registration
```

### Models

**Category** — groups videos by topic. Has a name, slug, and optional description.

**Video** — stores the title, slug, description, filename (the `.mp4` on disk), and an optional thumbnail and category. A `published` boolean controls visibility.

Videos are served from `/library/<filename>` — a directory on the server outside the Django project root, mapped in the web server configuration.

---

## Related Project

This video site exists to support users of the **[Djangify eCommerce Builder](https://github.com/djangify/ebuilder)** — a self-hosted, Docker-first digital downloads platform built with Django. The tutorials cover setup, configuration, and day-to-day use of that platform.

If you landed here looking for the main platform, that's the place to go.

---

## Features

- Category browsing with sidebar navigation
- Video detail pages with related video suggestions
- Optional thumbnail images per video
- Fully managed through Django Admin
- Mobile responsive
- No JavaScript framework required
- WhiteNoise for static file serving in production

---

## Environment Variables

Configuration is handled via a `.env` file using `django-environ`.

```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
```

---

## License

MIT — free to use, adapt, and build on.

---

## Author

Built by **Diane Corriette**

- GitHub: [@toDianeDev](https://github.com/toDianeDev)
- LinkedIn: [linkedin.com/in/todianedev](https://linkedin.com/in/todianedev)
