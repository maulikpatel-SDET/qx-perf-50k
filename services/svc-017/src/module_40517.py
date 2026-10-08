"""Service module 40517: business logic, no crypto."""


def calculate_total_40517(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40517():
    return 'module 40517 handles orders and invoices'
