"""Service module 32981: business logic, no crypto."""


def calculate_total_32981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32981():
    return 'module 32981 handles orders and invoices'
