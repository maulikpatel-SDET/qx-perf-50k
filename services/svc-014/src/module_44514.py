"""Service module 44514: business logic, no crypto."""


def calculate_total_44514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44514():
    return 'module 44514 handles orders and invoices'
