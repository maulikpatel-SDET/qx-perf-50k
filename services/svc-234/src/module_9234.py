"""Service module 9234: business logic, no crypto."""


def calculate_total_9234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9234():
    return 'module 9234 handles orders and invoices'
