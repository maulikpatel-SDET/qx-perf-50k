"""Service module 36854: business logic, no crypto."""


def calculate_total_36854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36854():
    return 'module 36854 handles orders and invoices'
