"""Service module 26497: business logic, no crypto."""


def calculate_total_26497(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26497():
    return 'module 26497 handles orders and invoices'
