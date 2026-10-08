"""Service module 32801: business logic, no crypto."""


def calculate_total_32801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32801():
    return 'module 32801 handles orders and invoices'
