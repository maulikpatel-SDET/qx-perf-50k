"""Service module 15607: business logic, no crypto."""


def calculate_total_15607(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15607():
    return 'module 15607 handles orders and invoices'
