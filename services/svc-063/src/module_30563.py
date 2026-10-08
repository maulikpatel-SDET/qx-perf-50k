"""Service module 30563: business logic, no crypto."""


def calculate_total_30563(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30563():
    return 'module 30563 handles orders and invoices'
