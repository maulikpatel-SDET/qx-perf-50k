"""Service module 36191: business logic, no crypto."""


def calculate_total_36191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36191():
    return 'module 36191 handles orders and invoices'
