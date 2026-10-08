"""Service module 34138: business logic, no crypto."""


def calculate_total_34138(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34138():
    return 'module 34138 handles orders and invoices'
