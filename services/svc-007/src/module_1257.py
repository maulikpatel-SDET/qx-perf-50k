"""Service module 1257: business logic, no crypto."""


def calculate_total_1257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1257():
    return 'module 1257 handles orders and invoices'
