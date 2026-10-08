"""Service module 33497: business logic, no crypto."""


def calculate_total_33497(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33497():
    return 'module 33497 handles orders and invoices'
