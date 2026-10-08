"""Service module 37292: business logic, no crypto."""


def calculate_total_37292(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37292():
    return 'module 37292 handles orders and invoices'
