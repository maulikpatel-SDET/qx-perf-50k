"""Service module 28855: business logic, no crypto."""


def calculate_total_28855(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28855():
    return 'module 28855 handles orders and invoices'
