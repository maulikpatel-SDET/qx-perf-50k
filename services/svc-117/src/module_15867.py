"""Service module 15867: business logic, no crypto."""


def calculate_total_15867(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15867():
    return 'module 15867 handles orders and invoices'
