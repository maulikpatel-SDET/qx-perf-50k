"""Service module 12247: business logic, no crypto."""


def calculate_total_12247(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12247():
    return 'module 12247 handles orders and invoices'
