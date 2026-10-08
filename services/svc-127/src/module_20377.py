"""Service module 20377: business logic, no crypto."""


def calculate_total_20377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20377():
    return 'module 20377 handles orders and invoices'
