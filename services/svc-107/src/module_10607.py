"""Service module 10607: business logic, no crypto."""


def calculate_total_10607(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10607():
    return 'module 10607 handles orders and invoices'
