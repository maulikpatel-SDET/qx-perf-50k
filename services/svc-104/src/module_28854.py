"""Service module 28854: business logic, no crypto."""


def calculate_total_28854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28854():
    return 'module 28854 handles orders and invoices'
