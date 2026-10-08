"""Service module 2414: business logic, no crypto."""


def calculate_total_2414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2414():
    return 'module 2414 handles orders and invoices'
