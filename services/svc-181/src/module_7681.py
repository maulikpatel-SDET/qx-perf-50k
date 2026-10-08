"""Service module 7681: business logic, no crypto."""


def calculate_total_7681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7681():
    return 'module 7681 handles orders and invoices'
