"""Service module 28968: business logic, no crypto."""


def calculate_total_28968(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28968():
    return 'module 28968 handles orders and invoices'
