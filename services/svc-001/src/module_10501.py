"""Service module 10501: business logic, no crypto."""


def calculate_total_10501(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10501():
    return 'module 10501 handles orders and invoices'
