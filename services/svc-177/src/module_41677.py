"""Service module 41677: business logic, no crypto."""


def calculate_total_41677(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41677():
    return 'module 41677 handles orders and invoices'
