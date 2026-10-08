"""Service module 19250: business logic, no crypto."""


def calculate_total_19250(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19250():
    return 'module 19250 handles orders and invoices'
