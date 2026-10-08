"""Service module 35854: business logic, no crypto."""


def calculate_total_35854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35854():
    return 'module 35854 handles orders and invoices'
