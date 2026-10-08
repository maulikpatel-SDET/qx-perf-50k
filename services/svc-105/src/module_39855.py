"""Service module 39855: business logic, no crypto."""


def calculate_total_39855(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39855():
    return 'module 39855 handles orders and invoices'
