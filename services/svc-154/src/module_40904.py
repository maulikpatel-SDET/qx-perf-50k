"""Service module 40904: business logic, no crypto."""


def calculate_total_40904(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40904():
    return 'module 40904 handles orders and invoices'
