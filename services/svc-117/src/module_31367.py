"""Service module 31367: business logic, no crypto."""


def calculate_total_31367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31367():
    return 'module 31367 handles orders and invoices'
