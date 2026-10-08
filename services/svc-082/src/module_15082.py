"""Service module 15082: business logic, no crypto."""


def calculate_total_15082(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15082():
    return 'module 15082 handles orders and invoices'
