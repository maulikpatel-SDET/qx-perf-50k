"""Service module 2418: business logic, no crypto."""


def calculate_total_2418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2418():
    return 'module 2418 handles orders and invoices'
