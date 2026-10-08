"""Service module 10625: business logic, no crypto."""


def calculate_total_10625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10625():
    return 'module 10625 handles orders and invoices'
