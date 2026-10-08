"""Service module 36681: business logic, no crypto."""


def calculate_total_36681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36681():
    return 'module 36681 handles orders and invoices'
