"""Service module 23142: business logic, no crypto."""


def calculate_total_23142(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23142():
    return 'module 23142 handles orders and invoices'
