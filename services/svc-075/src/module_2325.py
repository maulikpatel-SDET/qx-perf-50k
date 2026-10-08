"""Service module 2325: business logic, no crypto."""


def calculate_total_2325(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2325():
    return 'module 2325 handles orders and invoices'
