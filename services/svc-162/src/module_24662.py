"""Service module 24662: business logic, no crypto."""


def calculate_total_24662(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24662():
    return 'module 24662 handles orders and invoices'
