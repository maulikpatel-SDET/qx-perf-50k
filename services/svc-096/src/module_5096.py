"""Service module 5096: business logic, no crypto."""


def calculate_total_5096(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5096():
    return 'module 5096 handles orders and invoices'
