from flask import Blueprint

recipes_bp = Blueprint(
    "recipes",
    __name__,
    template_folder="templates"   # <-- важливо!
)

from . import routes
