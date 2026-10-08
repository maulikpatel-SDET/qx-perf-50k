"""Service module 35129: business logic, no crypto."""


def calculate_total_35129(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35129():
    return 'module 35129 handles orders and invoices'
