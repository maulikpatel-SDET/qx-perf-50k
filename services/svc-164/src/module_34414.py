"""Service module 34414: business logic, no crypto."""


def calculate_total_34414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34414():
    return 'module 34414 handles orders and invoices'
