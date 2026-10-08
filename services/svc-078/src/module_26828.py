"""Service module 26828: business logic, no crypto."""


def calculate_total_26828(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26828():
    return 'module 26828 handles orders and invoices'
