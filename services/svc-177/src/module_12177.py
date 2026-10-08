"""Service module 12177: business logic, no crypto."""


def calculate_total_12177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12177():
    return 'module 12177 handles orders and invoices'
