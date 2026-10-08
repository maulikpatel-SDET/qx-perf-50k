"""Service module 35411: business logic, no crypto."""


def calculate_total_35411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35411():
    return 'module 35411 handles orders and invoices'
