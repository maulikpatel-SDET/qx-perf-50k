"""Service module 441: business logic, no crypto."""


def calculate_total_441(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_441():
    return 'module 441 handles orders and invoices'
