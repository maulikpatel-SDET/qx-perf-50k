"""Service module 45391: business logic, no crypto."""


def calculate_total_45391(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45391():
    return 'module 45391 handles orders and invoices'
