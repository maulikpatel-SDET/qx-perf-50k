"""Service module 19980: business logic, no crypto."""


def calculate_total_19980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19980():
    return 'module 19980 handles orders and invoices'
