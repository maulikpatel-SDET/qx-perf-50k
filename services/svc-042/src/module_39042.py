"""Service module 39042: business logic, no crypto."""


def calculate_total_39042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39042():
    return 'module 39042 handles orders and invoices'
