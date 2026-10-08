"""Service module 367: business logic, no crypto."""


def calculate_total_367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_367():
    return 'module 367 handles orders and invoices'
