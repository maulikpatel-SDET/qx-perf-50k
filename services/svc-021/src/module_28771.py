"""Service module 28771: business logic, no crypto."""


def calculate_total_28771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28771():
    return 'module 28771 handles orders and invoices'
