"""Service module 28681: business logic, no crypto."""


def calculate_total_28681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28681():
    return 'module 28681 handles orders and invoices'
