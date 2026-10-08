"""Service module 16414: business logic, no crypto."""


def calculate_total_16414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16414():
    return 'module 16414 handles orders and invoices'
