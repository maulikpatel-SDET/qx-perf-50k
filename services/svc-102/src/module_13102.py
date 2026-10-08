"""Service module 13102: business logic, no crypto."""


def calculate_total_13102(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13102():
    return 'module 13102 handles orders and invoices'
