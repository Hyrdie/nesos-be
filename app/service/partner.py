from sqlalchemy.orm import Session
from app.orm.db_setup import engine
from app.schema.partner import DetailPartner, Menu, TimeOpen, Facility, Payment, Service
from app.repository.partner_detail import (
    get_detail_partner, 
    get_menu_partner, 
    get_time_open_partner,
    get_facility_partner,
    get_payment_partner,
    get_service_partner
)

def get_partner_detail(partner_id) -> DetailPartner:
    with Session(engine) as session:
        partner_data = get_detail_partner(session, partner_id).fetchone()
        partner_menu = get_menu_partner(session, partner_id)
        partner_time_open = get_time_open_partner(session, partner_id)
        partner_facility = get_facility_partner(session, partner_id)
        partner_payment = get_payment_partner(session, partner_id)
        partner_service = get_service_partner(session, partner_id)
    
    list_menu = []
    for menu in partner_menu:
        list_menu.append(Menu(name=menu.menu, price=menu.price))
    
    list_time_open = []
    for time in partner_time_open:
        list_time_open.append(TimeOpen(day_open=time.day_open, status_open=time.status_open, start_time=time.start_time, end_time=time.end_time))
    
    list_facility = []
    for facility in partner_facility:
        list_facility.append(Facility(name=facility.facility))
    
    list_payment = []
    for payment in partner_payment:
        list_payment.append(Payment(name=payment.payment))
    
    list_service = []
    for service in partner_service:
        list_service.append(Service(name=service.service))
    
    resp = DetailPartner(
        partner_name=partner_data.partner_name,
        category_name=partner_data.category_name,
        email=partner_data.email,
        menu=list_menu,
        time_open=list_time_open,
        facility=list_facility,
        payment=list_payment,
        service=list_service
    )

    return resp
