"""Service module 44517: business logic, no crypto."""


def calculate_total_44517(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44517():
    return 'module 44517 handles orders and invoices'
