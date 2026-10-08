"""Service module 1600: business logic, no crypto."""


def calculate_total_1600(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1600():
    return 'module 1600 handles orders and invoices'
