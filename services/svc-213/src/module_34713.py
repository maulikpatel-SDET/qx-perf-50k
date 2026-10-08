"""Service module 34713: business logic, no crypto."""


def calculate_total_34713(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34713():
    return 'module 34713 handles orders and invoices'
