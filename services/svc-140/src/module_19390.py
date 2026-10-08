"""Service module 19390: business logic, no crypto."""


def calculate_total_19390(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19390():
    return 'module 19390 handles orders and invoices'
