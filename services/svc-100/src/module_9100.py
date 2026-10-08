"""Service module 9100: business logic, no crypto."""


def calculate_total_9100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9100():
    return 'module 9100 handles orders and invoices'
