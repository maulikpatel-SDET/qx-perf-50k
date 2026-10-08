"""Service module 25904: business logic, no crypto."""


def calculate_total_25904(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25904():
    return 'module 25904 handles orders and invoices'
