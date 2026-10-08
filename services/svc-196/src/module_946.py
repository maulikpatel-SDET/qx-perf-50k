"""Service module 946: business logic, no crypto."""


def calculate_total_946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_946():
    return 'module 946 handles orders and invoices'
