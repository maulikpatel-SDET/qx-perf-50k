"""Service module 33979: business logic, no crypto."""


def calculate_total_33979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33979():
    return 'module 33979 handles orders and invoices'
