"""Service module 48867: business logic, no crypto."""


def calculate_total_48867(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48867():
    return 'module 48867 handles orders and invoices'
