"""Service module 22682: business logic, no crypto."""


def calculate_total_22682(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22682():
    return 'module 22682 handles orders and invoices'
