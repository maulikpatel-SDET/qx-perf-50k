"""Service module 41689: business logic, no crypto."""


def calculate_total_41689(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41689():
    return 'module 41689 handles orders and invoices'
