"""Service module 33397: business logic, no crypto."""


def calculate_total_33397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33397():
    return 'module 33397 handles orders and invoices'
