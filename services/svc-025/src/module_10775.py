"""Service module 10775: business logic, no crypto."""


def calculate_total_10775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10775():
    return 'module 10775 handles orders and invoices'
