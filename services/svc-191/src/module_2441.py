"""Service module 2441: business logic, no crypto."""


def calculate_total_2441(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2441():
    return 'module 2441 handles orders and invoices'
