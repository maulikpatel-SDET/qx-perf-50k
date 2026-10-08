"""Service module 31630: business logic, no crypto."""


def calculate_total_31630(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31630():
    return 'module 31630 handles orders and invoices'
