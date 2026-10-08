"""Service module 21177: business logic, no crypto."""


def calculate_total_21177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21177():
    return 'module 21177 handles orders and invoices'
