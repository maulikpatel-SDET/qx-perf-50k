"""Service module 22412: business logic, no crypto."""


def calculate_total_22412(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22412():
    return 'module 22412 handles orders and invoices'
