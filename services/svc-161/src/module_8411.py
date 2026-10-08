"""Service module 8411: business logic, no crypto."""


def calculate_total_8411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8411():
    return 'module 8411 handles orders and invoices'
