"""Service module 48284: business logic, no crypto."""


def calculate_total_48284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48284():
    return 'module 48284 handles orders and invoices'
