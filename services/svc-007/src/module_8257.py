"""Service module 8257: business logic, no crypto."""


def calculate_total_8257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8257():
    return 'module 8257 handles orders and invoices'
