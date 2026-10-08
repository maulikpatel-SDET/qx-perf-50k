"""Service module 48177: business logic, no crypto."""


def calculate_total_48177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48177():
    return 'module 48177 handles orders and invoices'
