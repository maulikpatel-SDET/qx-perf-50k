"""Service module 21540: business logic, no crypto."""


def calculate_total_21540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21540():
    return 'module 21540 handles orders and invoices'
