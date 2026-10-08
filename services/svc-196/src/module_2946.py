"""Service module 2946: business logic, no crypto."""


def calculate_total_2946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2946():
    return 'module 2946 handles orders and invoices'
