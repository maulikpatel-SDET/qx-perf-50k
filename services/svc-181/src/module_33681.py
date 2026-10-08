"""Service module 33681: business logic, no crypto."""


def calculate_total_33681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33681():
    return 'module 33681 handles orders and invoices'
