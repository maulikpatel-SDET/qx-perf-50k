"""Service module 11547: business logic, no crypto."""


def calculate_total_11547(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11547():
    return 'module 11547 handles orders and invoices'
