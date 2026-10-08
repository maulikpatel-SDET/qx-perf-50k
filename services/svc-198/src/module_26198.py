"""Service module 26198: business logic, no crypto."""


def calculate_total_26198(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26198():
    return 'module 26198 handles orders and invoices'
