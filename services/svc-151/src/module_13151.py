"""Service module 13151: business logic, no crypto."""


def calculate_total_13151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13151():
    return 'module 13151 handles orders and invoices'
