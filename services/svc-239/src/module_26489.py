"""Service module 26489: business logic, no crypto."""


def calculate_total_26489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26489():
    return 'module 26489 handles orders and invoices'
