"""Service module 12348: business logic, no crypto."""


def calculate_total_12348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12348():
    return 'module 12348 handles orders and invoices'
