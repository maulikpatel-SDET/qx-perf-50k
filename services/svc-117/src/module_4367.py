"""Service module 4367: business logic, no crypto."""


def calculate_total_4367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4367():
    return 'module 4367 handles orders and invoices'
