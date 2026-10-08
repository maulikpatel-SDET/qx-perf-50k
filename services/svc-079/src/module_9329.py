"""Service module 9329: business logic, no crypto."""


def calculate_total_9329(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9329():
    return 'module 9329 handles orders and invoices'
