"""Service module 29196: business logic, no crypto."""


def calculate_total_29196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29196():
    return 'module 29196 handles orders and invoices'
