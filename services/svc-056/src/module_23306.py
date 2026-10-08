"""Service module 23306: business logic, no crypto."""


def calculate_total_23306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23306():
    return 'module 23306 handles orders and invoices'
