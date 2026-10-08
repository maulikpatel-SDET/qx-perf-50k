"""Service module 46329: business logic, no crypto."""


def calculate_total_46329(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46329():
    return 'module 46329 handles orders and invoices'
