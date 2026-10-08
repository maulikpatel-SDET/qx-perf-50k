"""Service module 3441: business logic, no crypto."""


def calculate_total_3441(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3441():
    return 'module 3441 handles orders and invoices'
