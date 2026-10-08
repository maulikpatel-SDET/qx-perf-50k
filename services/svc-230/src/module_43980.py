"""Service module 43980: business logic, no crypto."""


def calculate_total_43980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43980():
    return 'module 43980 handles orders and invoices'
