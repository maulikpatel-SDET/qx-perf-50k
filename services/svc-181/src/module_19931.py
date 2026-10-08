"""Service module 19931: business logic, no crypto."""


def calculate_total_19931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19931():
    return 'module 19931 handles orders and invoices'
