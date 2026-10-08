"""Service module 24397: business logic, no crypto."""


def calculate_total_24397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24397():
    return 'module 24397 handles orders and invoices'
