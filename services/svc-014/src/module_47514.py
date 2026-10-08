"""Service module 47514: business logic, no crypto."""


def calculate_total_47514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47514():
    return 'module 47514 handles orders and invoices'
