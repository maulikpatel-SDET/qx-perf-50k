"""Service module 28946: business logic, no crypto."""


def calculate_total_28946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28946():
    return 'module 28946 handles orders and invoices'
