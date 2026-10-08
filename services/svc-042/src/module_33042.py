"""Service module 33042: business logic, no crypto."""


def calculate_total_33042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33042():
    return 'module 33042 handles orders and invoices'
