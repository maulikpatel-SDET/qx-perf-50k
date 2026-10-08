"""Service module 1211: business logic, no crypto."""


def calculate_total_1211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1211():
    return 'module 1211 handles orders and invoices'
