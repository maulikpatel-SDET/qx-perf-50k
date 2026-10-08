"""Service module 9853: business logic, no crypto."""


def calculate_total_9853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9853():
    return 'module 9853 handles orders and invoices'
