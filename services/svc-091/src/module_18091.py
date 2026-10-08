"""Service module 18091: business logic, no crypto."""


def calculate_total_18091(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18091():
    return 'module 18091 handles orders and invoices'
