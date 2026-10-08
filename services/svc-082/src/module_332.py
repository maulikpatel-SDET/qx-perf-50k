"""Service module 332: business logic, no crypto."""


def calculate_total_332(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_332():
    return 'module 332 handles orders and invoices'
