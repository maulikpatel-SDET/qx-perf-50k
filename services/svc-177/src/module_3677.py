"""Service module 3677: business logic, no crypto."""


def calculate_total_3677(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3677():
    return 'module 3677 handles orders and invoices'
