"""Service module 27377: business logic, no crypto."""


def calculate_total_27377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27377():
    return 'module 27377 handles orders and invoices'
