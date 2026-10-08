"""Service module 27980: business logic, no crypto."""


def calculate_total_27980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27980():
    return 'module 27980 handles orders and invoices'
