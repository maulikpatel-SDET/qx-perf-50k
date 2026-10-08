"""Service module 31209: business logic, no crypto."""


def calculate_total_31209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31209():
    return 'module 31209 handles orders and invoices'
