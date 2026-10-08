"""Service module 5100: business logic, no crypto."""


def calculate_total_5100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5100():
    return 'module 5100 handles orders and invoices'
