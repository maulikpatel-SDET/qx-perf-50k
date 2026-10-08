"""Service module 13367: business logic, no crypto."""


def calculate_total_13367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13367():
    return 'module 13367 handles orders and invoices'
