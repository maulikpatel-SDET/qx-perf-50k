"""Service module 9050: business logic, no crypto."""


def calculate_total_9050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9050():
    return 'module 9050 handles orders and invoices'
