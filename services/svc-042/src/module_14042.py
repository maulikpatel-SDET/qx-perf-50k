"""Service module 14042: business logic, no crypto."""


def calculate_total_14042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14042():
    return 'module 14042 handles orders and invoices'
