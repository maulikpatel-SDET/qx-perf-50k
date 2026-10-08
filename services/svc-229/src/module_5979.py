"""Service module 5979: business logic, no crypto."""


def calculate_total_5979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5979():
    return 'module 5979 handles orders and invoices'
