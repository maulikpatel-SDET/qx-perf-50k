"""Service module 18268: business logic, no crypto."""


def calculate_total_18268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18268():
    return 'module 18268 handles orders and invoices'
