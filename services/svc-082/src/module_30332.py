"""Service module 30332: business logic, no crypto."""


def calculate_total_30332(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30332():
    return 'module 30332 handles orders and invoices'
