"""Service module 38138: business logic, no crypto."""


def calculate_total_38138(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38138():
    return 'module 38138 handles orders and invoices'
