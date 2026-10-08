"""Service module 21238: business logic, no crypto."""


def calculate_total_21238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21238():
    return 'module 21238 handles orders and invoices'
