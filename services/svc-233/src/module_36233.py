"""Service module 36233: business logic, no crypto."""


def calculate_total_36233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36233():
    return 'module 36233 handles orders and invoices'
