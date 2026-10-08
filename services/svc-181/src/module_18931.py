"""Service module 18931: business logic, no crypto."""


def calculate_total_18931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18931():
    return 'module 18931 handles orders and invoices'
