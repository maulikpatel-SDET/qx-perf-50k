"""Service module 17563: business logic, no crypto."""


def calculate_total_17563(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17563():
    return 'module 17563 handles orders and invoices'
