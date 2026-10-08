"""Service module 9525: business logic, no crypto."""


def calculate_total_9525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9525():
    return 'module 9525 handles orders and invoices'
