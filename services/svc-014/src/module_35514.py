"""Service module 35514: business logic, no crypto."""


def calculate_total_35514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35514():
    return 'module 35514 handles orders and invoices'
