"""Service module 19550: business logic, no crypto."""


def calculate_total_19550(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19550():
    return 'module 19550 handles orders and invoices'
