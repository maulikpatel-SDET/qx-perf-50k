"""Service module 9489: business logic, no crypto."""


def calculate_total_9489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9489():
    return 'module 9489 handles orders and invoices'
