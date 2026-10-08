"""Service module 48194: business logic, no crypto."""


def calculate_total_48194(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48194():
    return 'module 48194 handles orders and invoices'
