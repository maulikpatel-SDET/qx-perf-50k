"""Service module 25981: business logic, no crypto."""


def calculate_total_25981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25981():
    return 'module 25981 handles orders and invoices'
