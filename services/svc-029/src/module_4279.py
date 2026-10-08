"""Service module 4279: business logic, no crypto."""


def calculate_total_4279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4279():
    return 'module 4279 handles orders and invoices'
