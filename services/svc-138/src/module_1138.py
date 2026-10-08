"""Service module 1138: business logic, no crypto."""


def calculate_total_1138(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1138():
    return 'module 1138 handles orders and invoices'
