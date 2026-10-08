"""Service module 28663: business logic, no crypto."""


def calculate_total_28663(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28663():
    return 'module 28663 handles orders and invoices'
