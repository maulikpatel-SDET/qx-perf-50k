"""Service module 27946: business logic, no crypto."""


def calculate_total_27946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27946():
    return 'module 27946 handles orders and invoices'
