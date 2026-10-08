"""Service module 5181: business logic, no crypto."""


def calculate_total_5181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5181():
    return 'module 5181 handles orders and invoices'
