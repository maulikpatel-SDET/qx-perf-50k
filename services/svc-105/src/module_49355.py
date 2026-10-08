"""Service module 49355: business logic, no crypto."""


def calculate_total_49355(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49355():
    return 'module 49355 handles orders and invoices'
