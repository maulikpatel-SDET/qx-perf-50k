"""Service module 24462: business logic, no crypto."""


def calculate_total_24462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24462():
    return 'module 24462 handles orders and invoices'
