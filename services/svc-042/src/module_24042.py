"""Service module 24042: business logic, no crypto."""


def calculate_total_24042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24042():
    return 'module 24042 handles orders and invoices'
