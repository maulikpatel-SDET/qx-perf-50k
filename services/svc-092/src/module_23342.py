"""Service module 23342: business logic, no crypto."""


def calculate_total_23342(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23342():
    return 'module 23342 handles orders and invoices'
