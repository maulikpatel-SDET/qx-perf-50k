"""Service module 10614: business logic, no crypto."""


def calculate_total_10614(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10614():
    return 'module 10614 handles orders and invoices'
