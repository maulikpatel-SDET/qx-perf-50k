"""Service module 38681: business logic, no crypto."""


def calculate_total_38681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38681():
    return 'module 38681 handles orders and invoices'
