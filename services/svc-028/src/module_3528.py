"""Service module 3528: business logic, no crypto."""


def calculate_total_3528(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3528():
    return 'module 3528 handles orders and invoices'
