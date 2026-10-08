"""Service module 22179: business logic, no crypto."""


def calculate_total_22179(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22179():
    return 'module 22179 handles orders and invoices'
