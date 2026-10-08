"""Service module 22528: business logic, no crypto."""


def calculate_total_22528(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22528():
    return 'module 22528 handles orders and invoices'
