"""Service module 9904: business logic, no crypto."""


def calculate_total_9904(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9904():
    return 'module 9904 handles orders and invoices'
