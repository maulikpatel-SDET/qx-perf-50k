"""Service module 41325: business logic, no crypto."""


def calculate_total_41325(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41325():
    return 'module 41325 handles orders and invoices'
