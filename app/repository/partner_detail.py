import sqlalchemy as sa

def get_detail_partner(session, id):
    sql = f"""
            select p.name as partner_name, c.name as category_name, p.official_open, p.telp, p.email, p.npwp, p.address, p.city, p.link_gmap
            from partner as p
            inner join category_partner cp on cp.partner_id = p.id 
            inner join category as c on c.id = cp.category_id
            where p.id='{id}' 
            and c.status_category = 'Main'
            """
    detail_partner = session.execute(sql)
    return detail_partner

def get_menu_partner(session, id):
    sql = f"""
            select p."name" as partner_name, m."name" as menu, m.price from partner p
            inner join menu_partner m on m.partner_id = p.id
            where m.partner_id = '{id}';
            """
    menu_partner = session.execute(sql)
    return menu_partner

def get_time_open_partner(session, id):
    sql = f"""
            select p.name as partner_name, to2."name" as day_open, top.status_open, top.start_time, top.end_time
            from partner p
            inner join time_open_partner top on top.partner_id = p.id
            inner join time_open to2 on to2.id=top.time_open_id 
            where p.id = '{id}'
            """
    time_open_partner = session.execute(sql)
    return time_open_partner

def get_facility_partner(session, id):
    sql = f"""
            select p.name as partner_name, c.name as facility from partner p 
            inner join category_partner cp on cp.partner_id = p.id
            inner join category c on c.id = cp.category_id 
            where c.status_category = 'Facility' 
            and cp.partner_id = '{id}';
            """
    data = session.execute(sql)
    return data

def get_payment_partner(session, id):
    sql = f"""
            select p.name as partner_name, c.name as payment from partner p 
            inner join category_partner cp on cp.partner_id = p.id
            inner join category c on c.id = cp.category_id 
            where c.status_category = 'Payment' 
            and cp.partner_id = '{id}';
            """
    data = session.execute(sql)
    return data

def get_service_partner(session, id):
    sql = f"""
            select p.name as partner_name, c.name as service from partner p 
            inner join category_partner cp on cp.partner_id = p.id
            inner join category c on c.id = cp.category_id 
            where c.status_category = 'Service' 
            and cp.partner_id = '{id}';
            """
    data = session.execute(sql)
    return data

