"""Service module 6964: business logic, no crypto."""


def calculate_total_6964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6964():
    return 'module 6964 handles orders and invoices'
