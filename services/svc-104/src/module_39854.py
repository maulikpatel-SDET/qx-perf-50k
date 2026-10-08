"""Service module 39854: business logic, no crypto."""


def calculate_total_39854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39854():
    return 'module 39854 handles orders and invoices'
