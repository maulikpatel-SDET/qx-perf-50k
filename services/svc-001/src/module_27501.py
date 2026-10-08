"""Service module 27501: business logic, no crypto."""


def calculate_total_27501(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27501():
    return 'module 27501 handles orders and invoices'
