"""Service module 2006: business logic, no crypto."""


def calculate_total_2006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2006():
    return 'module 2006 handles orders and invoices'
