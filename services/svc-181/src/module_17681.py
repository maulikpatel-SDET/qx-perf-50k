"""Service module 17681: business logic, no crypto."""


def calculate_total_17681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17681():
    return 'module 17681 handles orders and invoices'
