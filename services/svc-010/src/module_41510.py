"""Service module 41510: business logic, no crypto."""


def calculate_total_41510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41510():
    return 'module 41510 handles orders and invoices'
