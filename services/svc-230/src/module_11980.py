"""Service module 11980: business logic, no crypto."""


def calculate_total_11980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11980():
    return 'module 11980 handles orders and invoices'
