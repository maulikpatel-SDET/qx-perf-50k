"""Service module 8246: business logic, no crypto."""


def calculate_total_8246(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8246():
    return 'module 8246 handles orders and invoices'
