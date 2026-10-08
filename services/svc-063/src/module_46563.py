"""Service module 46563: business logic, no crypto."""


def calculate_total_46563(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46563():
    return 'module 46563 handles orders and invoices'
