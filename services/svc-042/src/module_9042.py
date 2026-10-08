"""Service module 9042: business logic, no crypto."""


def calculate_total_9042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9042():
    return 'module 9042 handles orders and invoices'
