"""Service module 16981: business logic, no crypto."""


def calculate_total_16981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16981():
    return 'module 16981 handles orders and invoices'
