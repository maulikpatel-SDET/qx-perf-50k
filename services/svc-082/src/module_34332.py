"""Service module 34332: business logic, no crypto."""


def calculate_total_34332(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34332():
    return 'module 34332 handles orders and invoices'
