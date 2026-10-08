"""Service module 24240: business logic, no crypto."""


def calculate_total_24240(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24240():
    return 'module 24240 handles orders and invoices'
