"""Service module 26681: business logic, no crypto."""


def calculate_total_26681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26681():
    return 'module 26681 handles orders and invoices'
