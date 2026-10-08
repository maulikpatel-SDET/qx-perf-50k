"""Service module 15177: business logic, no crypto."""


def calculate_total_15177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15177():
    return 'module 15177 handles orders and invoices'
