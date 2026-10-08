"""Service module 48166: business logic, no crypto."""


def calculate_total_48166(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48166():
    return 'module 48166 handles orders and invoices'
