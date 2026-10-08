"""Service module 33377: business logic, no crypto."""


def calculate_total_33377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33377():
    return 'module 33377 handles orders and invoices'
