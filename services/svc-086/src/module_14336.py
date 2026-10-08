"""Service module 14336: business logic, no crypto."""


def calculate_total_14336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14336():
    return 'module 14336 handles orders and invoices'
