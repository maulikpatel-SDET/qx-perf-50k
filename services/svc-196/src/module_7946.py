"""Service module 7946: business logic, no crypto."""


def calculate_total_7946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7946():
    return 'module 7946 handles orders and invoices'
