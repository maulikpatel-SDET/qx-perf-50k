"""Service module 44415: business logic, no crypto."""


def calculate_total_44415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44415():
    return 'module 44415 handles orders and invoices'
