"""Service module 10489: business logic, no crypto."""


def calculate_total_10489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10489():
    return 'module 10489 handles orders and invoices'
