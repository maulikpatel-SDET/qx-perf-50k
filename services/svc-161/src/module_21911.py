"""Service module 21911: business logic, no crypto."""


def calculate_total_21911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21911():
    return 'module 21911 handles orders and invoices'
