from flask import Blueprint, jsonify
from .models import Service, Incident, Team, EscalationPolicy

bp = Blueprint('main', __name__)

@bp.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([service.name for service in services])

@bp.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([{
        'id': incident.id,
        'service_id': incident.service_id,
        'status': incident.status
    } for incident in incidents])
