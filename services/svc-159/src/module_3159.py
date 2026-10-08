"""Service module 3159: business logic, no crypto."""


def calculate_total_3159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3159():
    return 'module 3159 handles orders and invoices'
