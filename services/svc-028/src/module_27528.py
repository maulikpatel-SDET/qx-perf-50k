"""Service module 27528: business logic, no crypto."""


def calculate_total_27528(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27528():
    return 'module 27528 handles orders and invoices'
