"""Service module 6563: business logic, no crypto."""


def calculate_total_6563(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6563():
    return 'module 6563 handles orders and invoices'
