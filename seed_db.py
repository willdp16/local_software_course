from app import create_app, db
from app.models import User, Quote, QuoteXML, LogEntry
from datetime import datetime
import json

app = create_app()

def parse_datetime(date_str):
    return datetime.fromisoformat(date_str)

with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Load data from JSON
    with open('current_db_state.json', 'r') as f:
        data = json.load(f)

    # Create Users
    users = []
    for user_data in data['users']:
        user = User(
            username=user_data['username'],
            email=user_data['email'],
            password_hash=user_data['password_hash'],
            role=user_data['role'],
            address=user_data['address'],
            phone=user_data['phone'],
            created_at=parse_datetime(user_data['created_at'])
        )
        users.append(user)
        db.session.add(user)
    db.session.commit()

    # Create Quotes
    quotes = []
    for quote_data in data['quotes']:
        quote = Quote(
            reference_number=quote_data['reference_number'],
            customer_name=quote_data['customer_name'],
            vehicle_registration=quote_data['vehicle_registration'],
            postcode=quote_data['postcode'],
            start_date=parse_datetime(quote_data['start_date']),
            created_by=quote_data['created_by'],
            customer_user_id=quote_data['customer_user_id'],
            created_at=parse_datetime(quote_data['created_at']),
            status=quote_data['status'],
            cover_type=quote_data['cover_type'],
            annual_total=quote_data['annual_total'],
            monthly_total=quote_data['monthly_total']
        )
        quotes.append(quote)
        db.session.add(quote)
    db.session.commit()

    # Create XMLs
    for xml_data in data['xmls']:
        xml = QuoteXML(
            quote_id=xml_data['quote_id'],
            xml_type=xml_data['xml_type'],
            xml_content=xml_data['xml_content'],
            timestamp=parse_datetime(xml_data['timestamp'])
        )
        db.session.add(xml)
    db.session.commit()

    # Create Logs
    for log_data in data['logs']:
        log = LogEntry(
            user_id=log_data['user_id'],
            quote_id=log_data['quote_id'],
            action=log_data['action'],
            timestamp=parse_datetime(log_data['timestamp']),
            details=log_data['details']
        )
        db.session.add(log)
    db.session.commit()

    print("Database seeded.")