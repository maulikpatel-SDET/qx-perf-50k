"""Service module 30686: business logic, no crypto."""


def calculate_total_30686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30686():
    return 'module 30686 handles orders and invoices'
