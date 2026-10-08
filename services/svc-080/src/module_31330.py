"""Service module 31330: business logic, no crypto."""


def calculate_total_31330(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31330():
    return 'module 31330 handles orders and invoices'
