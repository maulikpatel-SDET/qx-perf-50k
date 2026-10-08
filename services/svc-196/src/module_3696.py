"""Service module 3696: business logic, no crypto."""


def calculate_total_3696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3696():
    return 'module 3696 handles orders and invoices'
