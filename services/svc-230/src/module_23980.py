"""Service module 23980: business logic, no crypto."""


def calculate_total_23980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23980():
    return 'module 23980 handles orders and invoices'
