"""Service module 42528: business logic, no crypto."""


def calculate_total_42528(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42528():
    return 'module 42528 handles orders and invoices'
