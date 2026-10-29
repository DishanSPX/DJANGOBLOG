"""Seed 6 sample cybersecurity posts into the database.
Run: python manage.py shell -c "exec(open('seed/seed_posts.py', encoding='utf-8').read())"
"""
import json
from pathlib import Path
from django.core.files import File
from django.contrib.auth.models import User
from blog.models import Post, Category, Tag

base = Path("seed")
author = User.objects.filter(is_superuser=True).first() or User.objects.first()
for d in json.loads((base / "posts.json").read_text(encoding="utf-8")):
    cat, _ = Category.objects.get_or_create(name=d["category"])
    post, created = Post.objects.get_or_create(slug=d["slug"], defaults={"title": d["title"][:200], "content": d["content"], "status": "published", "category": cat, "author": author})
    if not created:
        post.title, post.content, post.status, post.category = d["title"][:200], d["content"], "published", cat
    if d["image"] and not post.cover_image:
        with open(base / "images" / d["image"], "rb") as f:
            post.cover_image.save(d["image"], File(f), save=False)
    post.save()
    post.tags.set([Tag.objects.get_or_create(name=t)[0] for t in d["tags"]])
    print("ok", post.slug)

# hide placeholder posts (kept, set to draft)
for p in Post.objects.filter(status="published"):
    t = p.title.strip()
    if len(set(t.lower().replace(" ", ""))) <= 2 or t.lower().startswith(("aaaa", "test", "hey im test")):
        p.status = "draft"; p.save(); print("draft", p.slug)
