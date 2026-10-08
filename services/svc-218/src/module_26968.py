"""Service module 26968: business logic, no crypto."""


def calculate_total_26968(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26968():
    return 'module 26968 handles orders and invoices'
