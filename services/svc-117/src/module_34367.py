"""Service module 34367: business logic, no crypto."""


def calculate_total_34367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34367():
    return 'module 34367 handles orders and invoices'
