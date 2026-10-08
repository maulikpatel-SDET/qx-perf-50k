"""Service module 911: business logic, no crypto."""


def calculate_total_911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_911():
    return 'module 911 handles orders and invoices'
