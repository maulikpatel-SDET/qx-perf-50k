"""Service module 45699: business logic, no crypto."""


def calculate_total_45699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45699():
    return 'module 45699 handles orders and invoices'
