"""Service module 21082: business logic, no crypto."""


def calculate_total_21082(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21082():
    return 'module 21082 handles orders and invoices'
