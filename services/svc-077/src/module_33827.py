"""Service module 33827: business logic, no crypto."""


def calculate_total_33827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33827():
    return 'module 33827 handles orders and invoices'
