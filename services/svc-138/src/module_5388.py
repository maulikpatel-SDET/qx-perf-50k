"""Service module 5388: business logic, no crypto."""


def calculate_total_5388(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5388():
    return 'module 5388 handles orders and invoices'
