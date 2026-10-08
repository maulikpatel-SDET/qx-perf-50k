"""Service module 49681: business logic, no crypto."""


def calculate_total_49681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49681():
    return 'module 49681 handles orders and invoices'
