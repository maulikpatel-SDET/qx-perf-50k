"""Service module 12194: business logic, no crypto."""


def calculate_total_12194(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12194():
    return 'module 12194 handles orders and invoices'
