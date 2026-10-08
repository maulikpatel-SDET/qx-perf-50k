"""Service module 681: business logic, no crypto."""


def calculate_total_681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_681():
    return 'module 681 handles orders and invoices'
