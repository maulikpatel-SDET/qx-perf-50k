"""Service module 13238: business logic, no crypto."""


def calculate_total_13238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13238():
    return 'module 13238 handles orders and invoices'
