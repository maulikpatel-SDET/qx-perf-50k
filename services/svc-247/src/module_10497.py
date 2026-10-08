"""Service module 10497: business logic, no crypto."""


def calculate_total_10497(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10497():
    return 'module 10497 handles orders and invoices'
