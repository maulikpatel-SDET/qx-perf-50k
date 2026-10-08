"""Service module 48609: business logic, no crypto."""


def calculate_total_48609(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48609():
    return 'module 48609 handles orders and invoices'
