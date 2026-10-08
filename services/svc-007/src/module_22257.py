"""Service module 22257: business logic, no crypto."""


def calculate_total_22257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22257():
    return 'module 22257 handles orders and invoices'
