"""Service module 20697: business logic, no crypto."""


def calculate_total_20697(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20697():
    return 'module 20697 handles orders and invoices'
