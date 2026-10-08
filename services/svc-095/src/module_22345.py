"""Service module 22345: business logic, no crypto."""


def calculate_total_22345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22345():
    return 'module 22345 handles orders and invoices'
