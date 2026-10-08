"""Service module 21414: business logic, no crypto."""


def calculate_total_21414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21414():
    return 'module 21414 handles orders and invoices'
