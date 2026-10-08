"""Service module 3683: business logic, no crypto."""


def calculate_total_3683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3683():
    return 'module 3683 handles orders and invoices'
