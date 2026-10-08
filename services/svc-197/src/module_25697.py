"""Service module 25697: business logic, no crypto."""


def calculate_total_25697(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25697():
    return 'module 25697 handles orders and invoices'
