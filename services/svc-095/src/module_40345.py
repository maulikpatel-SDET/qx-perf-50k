"""Service module 40345: business logic, no crypto."""


def calculate_total_40345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40345():
    return 'module 40345 handles orders and invoices'
