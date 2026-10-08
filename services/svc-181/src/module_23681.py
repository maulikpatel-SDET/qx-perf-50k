"""Service module 23681: business logic, no crypto."""


def calculate_total_23681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23681():
    return 'module 23681 handles orders and invoices'
