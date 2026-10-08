"""Service module 33177: business logic, no crypto."""


def calculate_total_33177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33177():
    return 'module 33177 handles orders and invoices'
