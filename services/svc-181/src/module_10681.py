"""Service module 10681: business logic, no crypto."""


def calculate_total_10681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10681():
    return 'module 10681 handles orders and invoices'
