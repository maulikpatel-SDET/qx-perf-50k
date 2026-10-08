"""Service module 14268: business logic, no crypto."""


def calculate_total_14268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14268():
    return 'module 14268 handles orders and invoices'
