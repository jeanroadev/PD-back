import pandas as pd
from .models import Service, Incident

def generate_csv_report():
    services = Service.query.all()
    data = [{'id': service.id, 'name': service.name} for service in services]
    df = pd.DataFrame(data)
    df.to_csv('services_report.csv', index=False)
