"""Service module 37663: business logic, no crypto."""


def calculate_total_37663(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37663():
    return 'module 37663 handles orders and invoices'
