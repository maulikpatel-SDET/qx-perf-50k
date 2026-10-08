"""Service module 4345: business logic, no crypto."""


def calculate_total_4345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4345():
    return 'module 4345 handles orders and invoices'
