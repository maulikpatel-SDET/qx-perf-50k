"""Service module 2683: business logic, no crypto."""


def calculate_total_2683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2683():
    return 'module 2683 handles orders and invoices'
