"""Service module 4257: business logic, no crypto."""


def calculate_total_4257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4257():
    return 'module 4257 handles orders and invoices'
