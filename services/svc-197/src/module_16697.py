"""Service module 16697: business logic, no crypto."""


def calculate_total_16697(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16697():
    return 'module 16697 handles orders and invoices'
