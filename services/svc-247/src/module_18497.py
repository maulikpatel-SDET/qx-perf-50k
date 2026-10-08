"""Service module 18497: business logic, no crypto."""


def calculate_total_18497(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18497():
    return 'module 18497 handles orders and invoices'
