"""Service module 41082: business logic, no crypto."""


def calculate_total_41082(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41082():
    return 'module 41082 handles orders and invoices'
