"""Service module 39268: business logic, no crypto."""


def calculate_total_39268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39268():
    return 'module 39268 handles orders and invoices'
