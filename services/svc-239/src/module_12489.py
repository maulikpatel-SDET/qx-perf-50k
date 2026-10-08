"""Service module 12489: business logic, no crypto."""


def calculate_total_12489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12489():
    return 'module 12489 handles orders and invoices'
