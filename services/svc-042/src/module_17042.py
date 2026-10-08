"""Service module 17042: business logic, no crypto."""


def calculate_total_17042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17042():
    return 'module 17042 handles orders and invoices'
