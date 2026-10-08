"""Service module 35171: business logic, no crypto."""


def calculate_total_35171(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35171():
    return 'module 35171 handles orders and invoices'
