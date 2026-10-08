"""Service module 48981: business logic, no crypto."""


def calculate_total_48981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48981():
    return 'module 48981 handles orders and invoices'
