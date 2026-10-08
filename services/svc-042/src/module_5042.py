"""Service module 5042: business logic, no crypto."""


def calculate_total_5042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5042():
    return 'module 5042 handles orders and invoices'
