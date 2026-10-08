"""Service module 38043: business logic, no crypto."""


def calculate_total_38043(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38043():
    return 'module 38043 handles orders and invoices'
