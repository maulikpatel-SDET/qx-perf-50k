"""Service module 38855: business logic, no crypto."""


def calculate_total_38855(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38855():
    return 'module 38855 handles orders and invoices'
