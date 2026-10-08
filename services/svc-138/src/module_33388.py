"""Service module 33388: business logic, no crypto."""


def calculate_total_33388(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33388():
    return 'module 33388 handles orders and invoices'
