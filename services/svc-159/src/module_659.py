"""Service module 659: business logic, no crypto."""


def calculate_total_659(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_659():
    return 'module 659 handles orders and invoices'
