"""Service module 25198: business logic, no crypto."""


def calculate_total_25198(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25198():
    return 'module 25198 handles orders and invoices'
