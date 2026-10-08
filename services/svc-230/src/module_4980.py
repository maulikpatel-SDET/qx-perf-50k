"""Service module 4980: business logic, no crypto."""


def calculate_total_4980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4980():
    return 'module 4980 handles orders and invoices'
