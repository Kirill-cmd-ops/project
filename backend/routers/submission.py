from flask import Blueprint, jsonify, request

from services.submission import get_all_submissions_service, create_submission_service

submission_router = Blueprint("data", __name__)


@submission_router.get("/data")
def get_all_submissions():
    return jsonify(get_all_submissions_service())


@submission_router.post("/data")
def create_submission():
    body = request.get_json()
    create_submission_service(body)
    return jsonify({"ok": True}), 201
