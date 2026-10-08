"""Service module 38137: business logic, no crypto."""


def calculate_total_38137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38137():
    return 'module 38137 handles orders and invoices'
