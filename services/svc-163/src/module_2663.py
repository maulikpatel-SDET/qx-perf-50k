"""Service module 2663: business logic, no crypto."""


def calculate_total_2663(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2663():
    return 'module 2663 handles orders and invoices'
