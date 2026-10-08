"""Service module 42042: business logic, no crypto."""


def calculate_total_42042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42042():
    return 'module 42042 handles orders and invoices'
