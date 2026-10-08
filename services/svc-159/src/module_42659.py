"""Service module 42659: business logic, no crypto."""


def calculate_total_42659(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42659():
    return 'module 42659 handles orders and invoices'
