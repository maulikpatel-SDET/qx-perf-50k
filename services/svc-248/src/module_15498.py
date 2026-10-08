"""Service module 15498: business logic, no crypto."""


def calculate_total_15498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15498():
    return 'module 15498 handles orders and invoices'
