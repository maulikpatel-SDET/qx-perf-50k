"""Service module 27146: business logic, no crypto."""


def calculate_total_27146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27146():
    return 'module 27146 handles orders and invoices'
