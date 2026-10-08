"""Service module 10911: business logic, no crypto."""


def calculate_total_10911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10911():
    return 'module 10911 handles orders and invoices'
