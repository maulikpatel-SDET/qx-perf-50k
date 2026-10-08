"""Service module 19911: business logic, no crypto."""


def calculate_total_19911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19911():
    return 'module 19911 handles orders and invoices'
