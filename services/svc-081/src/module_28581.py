"""Service module 28581: business logic, no crypto."""


def calculate_total_28581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28581():
    return 'module 28581 handles orders and invoices'
