"""Service module 25414: business logic, no crypto."""


def calculate_total_25414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25414():
    return 'module 25414 handles orders and invoices'
