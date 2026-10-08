"""Service module 41676: business logic, no crypto."""


def calculate_total_41676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41676():
    return 'module 41676 handles orders and invoices'
