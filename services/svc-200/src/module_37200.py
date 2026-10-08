"""Service module 37200: business logic, no crypto."""


def calculate_total_37200(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37200():
    return 'module 37200 handles orders and invoices'
