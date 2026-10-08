"""Service module 41854: business logic, no crypto."""


def calculate_total_41854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41854():
    return 'module 41854 handles orders and invoices'
