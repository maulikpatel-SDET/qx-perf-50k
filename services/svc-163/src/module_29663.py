"""Service module 29663: business logic, no crypto."""


def calculate_total_29663(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29663():
    return 'module 29663 handles orders and invoices'
