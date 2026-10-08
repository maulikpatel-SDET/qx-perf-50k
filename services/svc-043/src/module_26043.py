"""Service module 26043: business logic, no crypto."""


def calculate_total_26043(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26043():
    return 'module 26043 handles orders and invoices'
