"""Service module 16193: business logic, no crypto."""


def calculate_total_16193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16193():
    return 'module 16193 handles orders and invoices'
