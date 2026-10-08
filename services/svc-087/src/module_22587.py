"""Service module 22587: business logic, no crypto."""


def calculate_total_22587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22587():
    return 'module 22587 handles orders and invoices'
