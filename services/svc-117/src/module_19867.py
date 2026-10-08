"""Service module 19867: business logic, no crypto."""


def calculate_total_19867(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19867():
    return 'module 19867 handles orders and invoices'
