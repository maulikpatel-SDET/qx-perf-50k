"""Service module 4769: business logic, no crypto."""


def calculate_total_4769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4769():
    return 'module 4769 handles orders and invoices'
