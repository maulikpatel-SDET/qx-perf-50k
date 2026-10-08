"""Service module 6348: business logic, no crypto."""


def calculate_total_6348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6348():
    return 'module 6348 handles orders and invoices'
