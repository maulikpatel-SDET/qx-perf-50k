"""Service module 49981: business logic, no crypto."""


def calculate_total_49981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49981():
    return 'module 49981 handles orders and invoices'
