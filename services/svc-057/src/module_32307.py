"""Service module 32307: business logic, no crypto."""


def calculate_total_32307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32307():
    return 'module 32307 handles orders and invoices'
