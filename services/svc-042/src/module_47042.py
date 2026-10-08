"""Service module 47042: business logic, no crypto."""


def calculate_total_47042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47042():
    return 'module 47042 handles orders and invoices'
