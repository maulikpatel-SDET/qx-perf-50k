"""Service module 35563: business logic, no crypto."""


def calculate_total_35563(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35563():
    return 'module 35563 handles orders and invoices'
