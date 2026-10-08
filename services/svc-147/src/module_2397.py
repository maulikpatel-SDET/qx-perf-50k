"""Service module 2397: business logic, no crypto."""


def calculate_total_2397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2397():
    return 'module 2397 handles orders and invoices'
