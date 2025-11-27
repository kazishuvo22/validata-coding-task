from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from werkzeug.exceptions import BadRequest

from forms.bank_form import BankForm
from services import bank_services

routes = Blueprint("routes", __name__)

# GET all banks (JSON)
@routes.route("/api/banks", methods=["GET"])
def get_banks():
    banks = bank_services.fetch_all()
    return jsonify([
        {"id": b.id, "name": b.name, "location": b.location}
        for b in banks
    ])

# GET single bank (JSON)
@routes.route("/api/banks/<int:bank_id>", methods=["GET"])
def get_bank(bank_id):
    bank = bank_services.fetch_one(bank_id)
    return jsonify({"id": bank.id, "name": bank.name, "location": bank.location})

# CREATE bank (JSON)
@routes.route("/api/banks", methods=["POST"])
def api_create_bank():
    data = request.get_json(force=True, silent=True)
    if not data:
        raise BadRequest("Invalid JSON body.")

    name = data.get("name")
    location = data.get("location")

    if not name or not location:
        raise BadRequest("Both 'name' and 'location' are required.")

    bank = bank_services.create(name, location)
    return jsonify({"id": bank.id, "name": bank.name, "location": bank.location})

# UPDATE bank (JSON)
@routes.route("/api/banks/<int:bank_id>", methods=["PUT"])
def api_update_bank(bank_id):
    data = request.get_json(force=True, silent=True)
    if not data:
        raise BadRequest("Invalid JSON body.")

    name = data.get("name")
    location = data.get("location")

    if not name or not location:
        raise BadRequest("Both 'name' and 'location' are required.")

    bank = bank_services.update(bank_id, name, location)
    return jsonify({"id": bank.id, "name": bank.name, "location": bank.location})

# DELETE bank (JSON)
@routes.route("/api/banks/<int:bank_id>", methods=["DELETE"])
def api_delete_bank(bank_id):
    bank_services.delete(bank_id)
    return jsonify({"success": True})

# HTML Template Route (ONLY add bank page)
@routes.route("/create", methods=["GET", "POST"])
def create_bank_form():
    form = BankForm()

    if form.validate_on_submit():
        name = form.name.data.strip()
        location = form.location.data.strip()
        if not name or not location:
            # Optionally flash a message in HTML template
            form.name.errors.append("Name is required.")
            form.location.errors.append("Location is required.")
        else:
            bank_services.create(name, location)
            return redirect(url_for("routes.get_banks"))

    return render_template("create_bank.html", form=form)