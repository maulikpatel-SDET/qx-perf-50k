"""Service module 35453: business logic, no crypto."""


def calculate_total_35453(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35453():
    return 'module 35453 handles orders and invoices'
