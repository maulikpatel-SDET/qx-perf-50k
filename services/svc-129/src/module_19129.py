"""Service module 19129: business logic, no crypto."""


def calculate_total_19129(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19129():
    return 'module 19129 handles orders and invoices'
