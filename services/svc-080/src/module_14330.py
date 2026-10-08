"""Service module 14330: business logic, no crypto."""


def calculate_total_14330(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14330():
    return 'module 14330 handles orders and invoices'
