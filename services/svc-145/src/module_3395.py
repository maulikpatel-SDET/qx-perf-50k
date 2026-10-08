"""Service module 3395: business logic, no crypto."""


def calculate_total_3395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3395():
    return 'module 3395 handles orders and invoices'
