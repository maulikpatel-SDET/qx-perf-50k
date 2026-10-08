"""Service module 41073: business logic, no crypto."""


def calculate_total_41073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41073():
    return 'module 41073 handles orders and invoices'
