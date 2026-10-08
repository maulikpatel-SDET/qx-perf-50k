"""Service module 11397: business logic, no crypto."""


def calculate_total_11397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11397():
    return 'module 11397 handles orders and invoices'
