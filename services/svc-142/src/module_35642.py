"""Service module 35642: business logic, no crypto."""


def calculate_total_35642(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35642():
    return 'module 35642 handles orders and invoices'
