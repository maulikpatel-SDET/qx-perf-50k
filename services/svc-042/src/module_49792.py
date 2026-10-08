"""Service module 49792: business logic, no crypto."""


def calculate_total_49792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49792():
    return 'module 49792 handles orders and invoices'
