"""Service module 30946: business logic, no crypto."""


def calculate_total_30946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30946():
    return 'module 30946 handles orders and invoices'
