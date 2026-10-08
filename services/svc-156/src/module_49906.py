"""Service module 49906: business logic, no crypto."""


def calculate_total_49906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49906():
    return 'module 49906 handles orders and invoices'
