"""Service module 40125: business logic, no crypto."""


def calculate_total_40125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40125():
    return 'module 40125 handles orders and invoices'
