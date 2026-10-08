"""Service module 28348: business logic, no crypto."""


def calculate_total_28348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28348():
    return 'module 28348 handles orders and invoices'
