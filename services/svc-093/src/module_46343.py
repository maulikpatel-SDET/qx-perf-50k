"""Service module 46343: business logic, no crypto."""


def calculate_total_46343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46343():
    return 'module 46343 handles orders and invoices'
