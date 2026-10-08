"""Service module 25769: business logic, no crypto."""


def calculate_total_25769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25769():
    return 'module 25769 handles orders and invoices'
