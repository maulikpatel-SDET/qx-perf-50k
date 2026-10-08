"""Service module 29497: business logic, no crypto."""


def calculate_total_29497(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29497():
    return 'module 29497 handles orders and invoices'
