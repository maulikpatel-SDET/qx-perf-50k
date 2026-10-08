"""Service module 40592: business logic, no crypto."""


def calculate_total_40592(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40592():
    return 'module 40592 handles orders and invoices'
