"""Service module 12609: business logic, no crypto."""


def calculate_total_12609(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12609():
    return 'module 12609 handles orders and invoices'
