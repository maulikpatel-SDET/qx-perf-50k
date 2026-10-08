"""Service module 23376: business logic, no crypto."""


def calculate_total_23376(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23376():
    return 'module 23376 handles orders and invoices'
