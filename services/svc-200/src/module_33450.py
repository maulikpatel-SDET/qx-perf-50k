"""Service module 33450: business logic, no crypto."""


def calculate_total_33450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33450():
    return 'module 33450 handles orders and invoices'
