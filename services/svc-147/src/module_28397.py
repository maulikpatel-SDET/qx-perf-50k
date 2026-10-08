"""Service module 28397: business logic, no crypto."""


def calculate_total_28397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28397():
    return 'module 28397 handles orders and invoices'
