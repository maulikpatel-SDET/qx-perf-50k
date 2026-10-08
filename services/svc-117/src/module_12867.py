"""Service module 12867: business logic, no crypto."""


def calculate_total_12867(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12867():
    return 'module 12867 handles orders and invoices'
