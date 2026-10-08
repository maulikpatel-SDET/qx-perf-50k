"""Service module 904: business logic, no crypto."""


def calculate_total_904(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_904():
    return 'module 904 handles orders and invoices'
