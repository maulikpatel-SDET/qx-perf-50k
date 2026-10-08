"""Service module 26332: business logic, no crypto."""


def calculate_total_26332(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26332():
    return 'module 26332 handles orders and invoices'
