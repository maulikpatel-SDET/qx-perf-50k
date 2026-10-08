"""Service module 7854: business logic, no crypto."""


def calculate_total_7854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7854():
    return 'module 7854 handles orders and invoices'
