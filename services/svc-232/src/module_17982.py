"""Service module 17982: business logic, no crypto."""


def calculate_total_17982(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17982():
    return 'module 17982 handles orders and invoices'
