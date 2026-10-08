"""Service module 22043: business logic, no crypto."""


def calculate_total_22043(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22043():
    return 'module 22043 handles orders and invoices'
