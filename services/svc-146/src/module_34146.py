"""Service module 34146: business logic, no crypto."""


def calculate_total_34146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34146():
    return 'module 34146 handles orders and invoices'
