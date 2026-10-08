"""Service module 38911: business logic, no crypto."""


def calculate_total_38911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38911():
    return 'module 38911 handles orders and invoices'
