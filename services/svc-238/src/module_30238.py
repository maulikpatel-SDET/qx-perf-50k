"""Service module 30238: business logic, no crypto."""


def calculate_total_30238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30238():
    return 'module 30238 handles orders and invoices'
