"""Service module 31306: business logic, no crypto."""


def calculate_total_31306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31306():
    return 'module 31306 handles orders and invoices'
