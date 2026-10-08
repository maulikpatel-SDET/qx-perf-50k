"""Service module 12607: business logic, no crypto."""


def calculate_total_12607(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12607():
    return 'module 12607 handles orders and invoices'
