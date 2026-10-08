"""Service module 15348: business logic, no crypto."""


def calculate_total_15348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15348():
    return 'module 15348 handles orders and invoices'
