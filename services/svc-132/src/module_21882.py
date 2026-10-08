"""Service module 21882: business logic, no crypto."""


def calculate_total_21882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21882():
    return 'module 21882 handles orders and invoices'
