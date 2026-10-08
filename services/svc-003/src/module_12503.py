"""Service module 12503: business logic, no crypto."""


def calculate_total_12503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12503():
    return 'module 12503 handles orders and invoices'
