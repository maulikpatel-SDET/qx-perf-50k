"""Service module 39198: business logic, no crypto."""


def calculate_total_39198(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39198():
    return 'module 39198 handles orders and invoices'
