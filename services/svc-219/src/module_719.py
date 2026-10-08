"""Service module 719: business logic, no crypto."""


def calculate_total_719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_719():
    return 'module 719 handles orders and invoices'
