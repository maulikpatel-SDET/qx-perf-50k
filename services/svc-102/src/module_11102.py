"""Service module 11102: business logic, no crypto."""


def calculate_total_11102(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11102():
    return 'module 11102 handles orders and invoices'
