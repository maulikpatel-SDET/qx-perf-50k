"""Service module 1238: business logic, no crypto."""


def calculate_total_1238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1238():
    return 'module 1238 handles orders and invoices'
