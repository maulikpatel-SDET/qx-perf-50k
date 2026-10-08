"""Service module 4397: business logic, no crypto."""


def calculate_total_4397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4397():
    return 'module 4397 handles orders and invoices'
