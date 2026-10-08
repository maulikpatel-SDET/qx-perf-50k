"""Service module 8946: business logic, no crypto."""


def calculate_total_8946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8946():
    return 'module 8946 handles orders and invoices'
