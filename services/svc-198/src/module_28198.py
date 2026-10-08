"""Service module 28198: business logic, no crypto."""


def calculate_total_28198(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28198():
    return 'module 28198 handles orders and invoices'
