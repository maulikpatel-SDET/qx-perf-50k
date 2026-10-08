"""Service module 10527: business logic, no crypto."""


def calculate_total_10527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10527():
    return 'module 10527 handles orders and invoices'
