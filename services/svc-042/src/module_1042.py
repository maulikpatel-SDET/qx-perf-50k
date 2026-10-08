"""Service module 1042: business logic, no crypto."""


def calculate_total_1042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1042():
    return 'module 1042 handles orders and invoices'
