"""Service module 48528: business logic, no crypto."""


def calculate_total_48528(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48528():
    return 'module 48528 handles orders and invoices'
