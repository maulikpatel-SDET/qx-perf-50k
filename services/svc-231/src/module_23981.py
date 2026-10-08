"""Service module 23981: business logic, no crypto."""


def calculate_total_23981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23981():
    return 'module 23981 handles orders and invoices'
