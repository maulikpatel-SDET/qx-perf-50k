"""Service module 10904: business logic, no crypto."""


def calculate_total_10904(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10904():
    return 'module 10904 handles orders and invoices'
