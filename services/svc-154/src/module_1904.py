"""Service module 1904: business logic, no crypto."""


def calculate_total_1904(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1904():
    return 'module 1904 handles orders and invoices'
