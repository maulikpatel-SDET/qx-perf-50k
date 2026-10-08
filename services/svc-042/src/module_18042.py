"""Service module 18042: business logic, no crypto."""


def calculate_total_18042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18042():
    return 'module 18042 handles orders and invoices'
