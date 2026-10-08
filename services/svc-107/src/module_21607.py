"""Service module 21607: business logic, no crypto."""


def calculate_total_21607(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21607():
    return 'module 21607 handles orders and invoices'
