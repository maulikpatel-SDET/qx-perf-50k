"""Service module 25663: business logic, no crypto."""


def calculate_total_25663(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25663():
    return 'module 25663 handles orders and invoices'
