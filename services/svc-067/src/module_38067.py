"""Service module 38067: business logic, no crypto."""


def calculate_total_38067(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38067():
    return 'module 38067 handles orders and invoices'
