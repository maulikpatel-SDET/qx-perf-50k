"""Service module 5697: business logic, no crypto."""


def calculate_total_5697(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5697():
    return 'module 5697 handles orders and invoices'
