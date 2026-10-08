"""Service module 16198: business logic, no crypto."""


def calculate_total_16198(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16198():
    return 'module 16198 handles orders and invoices'
