"""Service module 15497: business logic, no crypto."""


def calculate_total_15497(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15497():
    return 'module 15497 handles orders and invoices'
