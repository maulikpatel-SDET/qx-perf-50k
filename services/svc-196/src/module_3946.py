"""Service module 3946: business logic, no crypto."""


def calculate_total_3946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3946():
    return 'module 3946 handles orders and invoices'
