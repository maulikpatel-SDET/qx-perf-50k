"""Service module 5332: business logic, no crypto."""


def calculate_total_5332(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5332():
    return 'module 5332 handles orders and invoices'
