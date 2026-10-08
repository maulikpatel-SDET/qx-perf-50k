"""Service module 21687: business logic, no crypto."""


def calculate_total_21687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21687():
    return 'module 21687 handles orders and invoices'
