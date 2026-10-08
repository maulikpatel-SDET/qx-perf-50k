"""Service module 10654: business logic, no crypto."""


def calculate_total_10654(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10654():
    return 'module 10654 handles orders and invoices'
