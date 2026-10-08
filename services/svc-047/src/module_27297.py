"""Service module 27297: business logic, no crypto."""


def calculate_total_27297(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27297():
    return 'module 27297 handles orders and invoices'
