"""Service module 8609: business logic, no crypto."""


def calculate_total_8609(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8609():
    return 'module 8609 handles orders and invoices'
