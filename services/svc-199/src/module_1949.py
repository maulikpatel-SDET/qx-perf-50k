"""Service module 1949: business logic, no crypto."""


def calculate_total_1949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1949():
    return 'module 1949 handles orders and invoices'
