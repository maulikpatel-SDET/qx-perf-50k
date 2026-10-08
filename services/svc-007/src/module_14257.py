"""Service module 14257: business logic, no crypto."""


def calculate_total_14257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14257():
    return 'module 14257 handles orders and invoices'
