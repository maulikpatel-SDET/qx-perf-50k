"""Service module 10882: business logic, no crypto."""


def calculate_total_10882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10882():
    return 'module 10882 handles orders and invoices'
