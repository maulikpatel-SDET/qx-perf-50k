"""Service module 563: business logic, no crypto."""


def calculate_total_563(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_563():
    return 'module 563 handles orders and invoices'
