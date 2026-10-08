"""Service module 1241: business logic, no crypto."""


def calculate_total_1241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1241():
    return 'module 1241 handles orders and invoices'
