"""Service module 44146: business logic, no crypto."""


def calculate_total_44146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44146():
    return 'module 44146 handles orders and invoices'
