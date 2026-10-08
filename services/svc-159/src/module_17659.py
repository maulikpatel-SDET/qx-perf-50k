"""Service module 17659: business logic, no crypto."""


def calculate_total_17659(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17659():
    return 'module 17659 handles orders and invoices'
