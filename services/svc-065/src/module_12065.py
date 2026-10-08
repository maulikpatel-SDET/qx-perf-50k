"""Service module 12065: business logic, no crypto."""


def calculate_total_12065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12065():
    return 'module 12065 handles orders and invoices'
